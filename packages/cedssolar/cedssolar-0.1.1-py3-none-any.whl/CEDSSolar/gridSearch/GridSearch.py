import datetime
from typing import Any
from . import fit
from .results import aggregate_across_months, GridSearchResults
from ..soda.soda import SolarSite
import calendar
import pandas as pd
import pvlib
import numpy as np
import tqdm
from sklearn.metrics import mean_absolute_error, mean_squared_error
from multiprocess import Pool
from bayes_opt import BayesianOptimization


def myprogress(
    curr: int,
    N: int,
    width: int = 10,
    bars: str = "▉▊▋▌▍▎▏ "[::-1],
    full: str = "█",
    empty: str = " ",
) -> str:
    """Progress bar for the tqdm class.


    Args:
        curr (int): The current index.
        N (int): The total number of indices.
        width (int, optional): The width of the progress indicator. Defaults to 10.
        bars (_type_, optional): The progress indicator bars. Defaults to "▉▊▋▌▍▎▏ "[::-1].
        full (str, optional): The bar to indicate once the computation at the index is completed. Defaults to "█".
        empty (str, optional): The bar to indicate at the start of the computation at the current index. Defaults to " ".

    Returns:
        str: The progress indicator.
    """
    p = curr / N
    nfull = int(p * width)
    return "{:>3.0%} |{}{}{}| {:>2}/{}".format(
        p,
        full * nfull,
        bars[int(len(bars) * ((p * width) % 1))],
        empty * (width - nfull - 1),
        curr,
        N,
    )


class SolarPVMetaData:
    """The Solar Metadata Data inference class.

    Args:
        data (pd.DataFrame): The data containing solar generation for a year.
        lat (float): The latitude at which the data was collected.
        lon (float): The longitude at which the data was collected.
        interval (str, optional): The time interval in minutes for the NSRDB data. For example: '30' is half hour intervals.
        Valid intervals are 30 & 60. Defaults to "30".
        tz (str, optional): The time zone at the location where the data was collected. Defaults to "US/Pacific".
    """

    def __init__(
        self,
        data: pd.DataFrame,
        lat: float,
        lon: float,
        interval: str = "30",
        tz: str = "US/Pacific",
    ) -> None:
        self.data = data
        self.lat = lat
        self.lon = lon
        self.interval = interval
        self.tz = tz

        self.solar_constant = 1366.1
        self.method = "nrel"  # //TODO: Changed from "spencer"
        self.model_airmass = "kastenyoung1989"
        self.albedo = 0.2
        self.surface_type = None
        self.model = "perez"
        self.model_perez = "allsitescomposite1990"
        self.zenith_filter = 70
        self.prepare_data()
        self.set_monthly_clearest_sky_data()

    def prepare_data(self) -> None:
        """Preprocess the data according to the needs. Here, we are adding irradiance data from NSRDB and solar positions
        to each data point.
        """
        self.data[["ghi", "dhi", "dni"]] = self._get_irradiance_data(
            self.lat, self.lon, self.interval
        )
        self._set_tz(self.tz)
        self.data[["zenith", "azimuth"]] = self._get_solar_position(self.lat, self.lon)

    def _get_irradiance_data(
        self, lat: float, lon: float, interval: str = "30"
    ) -> pd.DataFrame:
        """Query NSRDB for the irradiance data.

        Args:lat (float): The latitude at which the data was collected.
        lon (float): The longitude at which the data was collected.
        interval (str, optional): The time interval in minutes for the NSRDB data. For example: '30' is half hour intervals.

        Returns:
            pd.DataFrame: The irradiance data.
        """
        site = SolarSite(lat, lon)
        nsrdb = []

        for year in self.data.index.year.unique().tolist():
            nsrdb.append(
                site.get_nsrdb_data(
                    year=year,
                    leap_year=calendar.isleap(year),
                    interval=interval,
                    utc=False,
                )
            )
        nsrdb_df = pd.concat(nsrdb, axis=0)
        return nsrdb_df.iloc[
            nsrdb_df.index.get_indexer(self.data.index, method="nearest")
        ][["GHI", "DHI", "DNI"]]

    def _get_solar_position(self, lat: float, lon: float) -> pd.DataFrame:
        """Query pvlib for the solar position at the given latitude and longitude.

        Args:
            lat (float): The latitude at which the data was collected.
            lon (float): The longitude at which the data was collected.

        Returns:
            pd.DataFrame: The solar position data.
        """
        return pvlib.solarposition.get_solarposition(self.data.index, lat, lon)[
            ["apparent_zenith", "azimuth"]
        ]

    def _set_tz(self, tz: str = "US/Pacific") -> None:
        """Make the index a time range at the given time zone.

        Args:
            tz (str, optional): The time zone at the location where the data was collected. Defaults to "US/Pacific".
        """
        time = pd.date_range(
            start=self.data.index[0],
            end=self.data.index[-1],
            freq="1h",
            tz=tz,
        )
        self.data.index = time.rename("time")

    def set_monthly_clearest_sky_data(self) -> None:
        """Get the date points for the clearest day of each month."""
        self._get_daily_clear_sky_index()
        self._get_clearest_day_of_month()
        clearest_day_of_month_data = self.data.loc[
            np.isin(self.data.index.date, self.clearest_day_of_month.values.tolist())
        ]
        self.clearest_day_of_month_data = clearest_day_of_month_data.groupby(
            clearest_day_of_month_data.index.month, group_keys=True
        ).apply(pd.DataFrame)

    def _get_daily_clear_sky_index(self) -> None:
        """Get the clear sky index for each day. The clear sky index is the ratio of the total diffuse (DHI) and the
        total global horizontal irradiances (GHI) for that day.
        """
        GHI_daily = self.data["ghi"].resample("1D").sum().rename("daily_ghi")
        DHI_daily = self.data["dhi"].resample("1D").sum().rename("daily_dhi")
        self.clear_sky_index = (DHI_daily / GHI_daily).rename("clear_sky_index")

    def _get_clearest_day_of_month(self) -> None:
        """Calculate the clearest day of each month. The clearest day of a month is the day with the least clear sky index in the
        month.
        """
        self.clearest_day_of_month = (
            self.clear_sky_index.groupby(self.clear_sky_index.index.month)
            .idxmin()
            .apply(lambda w: w.date)
            .rename("clearestDayOfMonth")
            .rename_axis(index="month")
        )  # .apply(lambda w: w.strftime("%Y-%m-%d"))

    def monthly_clearest_day(self, month: int) -> datetime.date:
        """Get the clearest day of the given month.

        Args:
            month (int): The month.

        Returns:
            datetime.date: The clearest day of the given month.
        """
        assert 1 <= month <= 12, f"Month {month} not in range [1, 12]."
        return self.clearest_day_of_month.xs(month)

    def monthly_clearest_day_data(self, month: int) -> pd.DataFrame:
        """Get the data for the clearest day of the given month.

        Args:
            month (int): The month.

        Returns:
            pd.DataFrame: The data for the clearest day of the given month.
        """
        assert 1 <= month <= 12, f"Month {month} not in range [1, 12]."
        return self.clearest_day_of_month_data.xs(month)

    def _monthly_grid_search(self, args: dict[str, Any]) -> GridSearchResults:
        """Perform a grid search to find the best fit for all the months.

        Args:
            args (dict[str, Any]): The dictionary of the month's index and the lists of the surface tilt and azimuths to search.

        Returns:
            GridSearchResults: A dataframe containing the RMSE and MAE between the normalized solar generation and the normalized
            total solar irradiation at the given location and time.
        """
        month = args["month"]
        surface_tilt_list = args["surface_tilt_list"]
        surface_azimuth_list = args["surface_azimuth_list"]
        assert 1 <= month <= 12, f"Month {month} not in range [1, 12]."

        monthly_data = self.monthly_clearest_day_data(month)
        day_of_year = self.monthly_clearest_day(month)
        dni_extra = pvlib.irradiance.get_extra_radiation(
            datetime_or_doy=day_of_year,
            solar_constant=self.solar_constant,
            method=self.method,
            epoch_year=day_of_year.year,
        )
        air_mass = pvlib.atmosphere.get_relative_airmass(
            zenith=monthly_data.zenith, model=self.model_airmass
        ).fillna(0)

        power_norm = (monthly_data.W - monthly_data.W.min()) / (
            monthly_data.W.max() - monthly_data.W.min()
        )

        result_df = pd.DataFrame(
            columns=["surface_azimuth", "surface_tilt", "RMSE", "MAE"]
        )

        surface_tilt_bar = tqdm.tqdm(
            surface_tilt_list,
            bar_format="{l_bar}{bar:10}{r_bar}{bar:-10b}",
            disable=True,
        )

        for surface_tilt in surface_tilt_bar:
            for surface_azimuth_idx, surface_azimuth in enumerate(surface_azimuth_list):
                surface_tilt_bar.set_postfix_str(
                    myprogress(surface_azimuth_idx, len(surface_azimuth_list))
                )
                poa_cal = pvlib.irradiance.get_total_irradiance(
                    surface_tilt=surface_tilt,
                    surface_azimuth=surface_azimuth,
                    solar_zenith=monthly_data.zenith,
                    solar_azimuth=monthly_data.azimuth,
                    dni=monthly_data.dni,
                    ghi=monthly_data.ghi,
                    dhi=monthly_data.dhi,
                    dni_extra=dni_extra,
                    airmass=air_mass,
                    albedo=self.albedo,
                    surface_type=self.surface_type,
                    model=self.model,
                    model_perez=self.model_perez,
                )
                poa_norm = (poa_cal["poa_global"] - poa_cal["poa_global"].min()) / (
                    poa_cal["poa_global"].max() - poa_cal["poa_global"].min()
                )
                MAE = mean_absolute_error(
                    power_norm.loc[monthly_data.zenith < self.zenith_filter],
                    poa_norm.loc[monthly_data.zenith < self.zenith_filter],
                )
                RMSE = mean_squared_error(
                    power_norm.loc[monthly_data.zenith < self.zenith_filter],
                    poa_norm.loc[monthly_data.zenith < self.zenith_filter],
                    squared=False,
                )
                result_df.loc[len(result_df)] = [
                    surface_azimuth,
                    surface_tilt,
                    RMSE,
                    MAE,
                ]
        return result_df

    def monthly_grid_search(
        self,
        months: list[int] = range(1, 13),
        surface_tilt_list: list[float] = range(0, 91, 1),
        surface_azimuth_list: list[float] = range(0, 360, 1),
    ) -> list[GridSearchResults]:
        """Perform a monthly grid search for the given months, suraface tilts and azimuths.

        Args:
            months (list[int], optional): The list of months. Defaults to range(1, 13).
            surface_tilt_list (list[float], optional): The list of surface tilts. Defaults to range(0, 91, 1).
            surface_azimuth_list (list[float], optional): The list of surface azimuths. Defaults to range(0, 360, 1)

        Returns:
            list[GridSearchResults]: The list of grid search metrics. Each element in the list is a dataframe containing the RMSE
            and MAE between the normalized solar generation and the normalized total solar irradiation at the given location and time.
        """
        args = tuple(
            [
                {
                    "month": month,
                    "surface_tilt_list": surface_tilt_list,
                    "surface_azimuth_list": surface_azimuth_list,
                }
                for month in months
            ]
        )
        results = list()
        pool = Pool(processes=6)
        pool.map_async(self._monthly_grid_search, args, callback=results.append)
        pool.close()
        pool.join()
        return results[0]

    def smart_grid_search(
        self, top_percent_to_retain_per_month: float = 0.1, rmse_filtered: bool = True
    ) -> list[GridSearchResults]:
        """Perform a smart grid search.

        Args:
            top_percent_to_retain_per_month (float, optional): The percent of (azimuth, tilt) pairs to retain in each month. Defaults to 0.1.
            rmse_filtered (bool, optional): Whether to filter based on the RMSE of the fit. Defaults to True.

        Returns:
            list[GridSearchResults]: The list of monthly results.
        """
        tiltmin, tiltmax, tiltdelta = 0, 91, 5
        azimuthmin, azimuthmax, azimuthdelta = 0, 360, 15
        yearly_results_list = []
        for _ in range(2):
            results = self.monthly_grid_search(
                surface_tilt_list=np.arange(tiltmin, tiltmax, tiltdelta),
                surface_azimuth_list=np.arange(azimuthmin, azimuthmax, azimuthdelta),
            )
            # results_filt = filter_grid_search_results(
            #     results, p=top_percent_to_retain_per_month
            # )
            # //TODO: results_filt is now taken care off in the
            # aggregate_across_months method. Can remove after testing.
            yearly_results = aggregate_across_months(
                monthly_results=results,
                top_percent_to_retain_per_month=top_percent_to_retain_per_month,
                rmse_filtered=rmse_filtered,
            )
            best_fit = fit.best_fit(yearly_results)
            tiltmin, tiltmax, tiltdelta = (
                int(best_fit.tilt - tiltdelta),
                int(best_fit.tilt + tiltdelta),
                1,
            )
            azimuthmin, azimuthmax, azimuthdelta = (
                int(best_fit.azimuth - azimuthdelta),
                int(best_fit.azimuth + azimuthdelta),
                1,
            )
            yearly_results_list.append(yearly_results)
        return yearly_results_list

    def black_box_function(self, surface_azimuth: float, surface_tilt: float) -> float:
        """The function used by the Bayesian optimizer. It return the -(RMSE + MAE) between the normalized solar generation
        and the normalized total solar irradiation at the given surface azimuth and tilt, location and time.

        Args:
            surface_azimuth (float): The surface azimuth.
            surface_tilt (float): The surface tilt.

        Returns:
            float: The -(RMSE + MAE) between the normalized solar generation and the normalized total solar irradiation
            at the given surface azimuth and tilt, location and time.
        """
        RMSE, MAE = 0, 0
        for month in range(1, 13):
            monthly_data = self.monthly_clearest_day_data(month)
            day_of_year = self.monthly_clearest_day(month)
            dni_extra = pvlib.irradiance.get_extra_radiation(
                datetime_or_doy=day_of_year,
                solar_constant=self.solar_constant,
                method=self.method,
                epoch_year=day_of_year.year,
            )
            air_mass = pvlib.atmosphere.get_relative_airmass(
                zenith=monthly_data.zenith, model=self.model_airmass
            ).fillna(0)

            power_norm = (monthly_data.W - monthly_data.W.min()) / (
                monthly_data.W.max() - monthly_data.W.min()
            )

            poa_cal = pvlib.irradiance.get_total_irradiance(
                surface_tilt=surface_tilt,
                surface_azimuth=surface_azimuth,
                solar_zenith=monthly_data.zenith,
                solar_azimuth=monthly_data.azimuth,
                dni=monthly_data.dni,
                ghi=monthly_data.ghi,
                dhi=monthly_data.dhi,
                dni_extra=dni_extra,
                airmass=air_mass,
                albedo=self.albedo,
                surface_type=self.surface_type,
                model=self.model,
                model_perez=self.model_perez,
            )
            poa_norm = (poa_cal["poa_global"] - poa_cal["poa_global"].min()) / (
                poa_cal["poa_global"].max() - poa_cal["poa_global"].min()
            )
            MAE += mean_absolute_error(
                power_norm.loc[monthly_data.zenith < self.zenith_filter],
                poa_norm.loc[monthly_data.zenith < self.zenith_filter],
            )
            RMSE += mean_squared_error(
                power_norm.loc[monthly_data.zenith < self.zenith_filter],
                poa_norm.loc[monthly_data.zenith < self.zenith_filter],
                squared=False,
            )
        return -(RMSE + MAE)

    def bayesian_search(
        self,
        surface_azimuth: tuple[float, float],
        surface_tilt: tuple[float, float],
        optimizer_kwargs: dict,
        maximize_kwargs: dict,
    ) -> BayesianOptimization:
        """Perform the Bayesian search on the given range for surface azimuth and tilts.

        Args:
            surface_azimuth (tuple[float, float]): The lower and upper bound for the surface azimuth.
            surface_tilt (tuple[float, float]): The lower and upper bound for the surface tilt.
            optimizer_kwargs (dict): Extra arguments to be passed to the Bayesian Optimizer.
            maximize_kwargs (dict): Extra arguments to be passed to the maximizer.

        Returns:
            BayesianOptimization: The solved optimizer.
        """
        pbounds = {"surface_azimuth": surface_azimuth, "surface_tilt": surface_tilt}
        optimizer = BayesianOptimization(
            f=self.black_box_function,
            pbounds=pbounds,
            verbose=1,  # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
            # random_state=1,
            **optimizer_kwargs,
        )
        optimizer.maximize(**maximize_kwargs)
        return optimizer
