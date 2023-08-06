from multiprocessing.util import abstract_sockets_supported
from typing import Literal
from ..soda.soda import SolarSite
import calendar
import pandas as pd
import pvlib
import numpy as np
from tqdm import tqdm
from pydantic.dataclasses import dataclass
from multiprocess import Pool
from itertools import product

MODEL_AIRMASS_OPTIONS = Literal[
    "simple",
    "kasten1966",
    "youngirvine1967",
    "kastenyoung1989",
    "gueymard1993",
    "young1994",
    "pickering2002",
]
METHOD_OPTIONS = Literal["pyephem", "spencer", "asce", "nrel"]
MODEL_OPTIONS = Literal["isotropic", "klucher", "haydavies", "reindl", "king", "perez"]
MODEL_PEREZ_OPTIONS = Literal[
    "1990",
    "allsitescomposite1990",
    "allsitescomposite1988",
    "sandiacomposite1988",
    "usacomposite1988",
    "france1988",
    "phoenix1988",
    "elmonte1988",
    "osage1988",
    "albuquerque1988",
    "capecanaveral1988",
    "albany1988",
]


@dataclass
class PVLIBCONFIG:
    model_airmass: MODEL_AIRMASS_OPTIONS = "kastenyoung1989"
    method: METHOD_OPTIONS = "nrel"
    solar_constant: float = 1366.1
    albedo: float = 0.2
    surface_type = None
    model: MODEL_OPTIONS = "perez"
    model_perez: MODEL_PEREZ_OPTIONS = "allsitescomposite1990"


class Location:
    def __init__(
        self,
        lat: float,
        lon: float,
        tz: str = "America/Los_Angeles",
    ):
        self.lat = lat
        self.lon = lon
        self.tz = tz

    def daily_average_poa_Year(
        self,
        year: int,
        interval: Literal["30", "60"] = "60",
        pvlibconfig: PVLIBCONFIG = PVLIBCONFIG(),
    ):
        print("Getting time stamps...", end="")
        data = pd.DataFrame(
            pd.date_range(
                str(year),
                str(year + 1),
                freq="1H",
                tz=self.tz,
                name="datetime",
                inclusive="left",
            )
        ).set_index("datetime")
        print("Done.")
        print("Getting irradiation...", end="")
        data[["ghi", "dhi", "dni"]] = (
            SolarSite(self.lat, self.lon)
            .get_nsrdb_data(
                year=str(year),
                leap_year=calendar.isleap(year),
                interval=interval,
                utc=False,
            )[["GHI", "DHI", "DNI"]]
            .values
        )
        print("Done.")
        print("Getting solar position...", end="")
        data[["zenith", "azimuth"]] = pvlib.solarposition.get_solarposition(
            data.index, self.lat, self.lon
        )[["apparent_zenith", "azimuth"]]
        print("Done.")
        print("Building argument pairs...", end="")
        args = tuple(
            [
                (data.loc[day.strftime("%Y-%m-%d")], tilt, azimuth, pvlibconfig)
                for day, tilt, azimuth in tuple(
                    product(
                        np.unique(data.index.date), range(0, 91, 5), range(0, 361, 15)
                    )
                )
            ]
        )
        print("Done.")
        pool = Pool(processes=6)
        res_list = []
        with tqdm(total=len(args)) as pbar:
            for i, res in tqdm(enumerate(pool.imap_unordered(daily_average_poa, args))):
                pbar.update()
                res_list.append(res)
        pbar.close()
        pool.close()
        pool.join()
        return res_list


def daily_average_poa(args):
    data: pd.DataFrame = args[0]
    surface_tilt: float = args[1]
    surface_azimuth: float = args[2]
    pvlibconfig: PVLIBCONFIG = args[3]
    datetime_or_doy = np.unique(data.index.date)[0]
    dni_extra = pvlib.irradiance.get_extra_radiation(
        datetime_or_doy=datetime_or_doy,
        solar_constant=pvlibconfig.solar_constant,
        method=pvlibconfig.method,
        epoch_year=datetime_or_doy.year,
    )
    air_mass = pvlib.atmosphere.get_relative_airmass(
        zenith=data.zenith, model=pvlibconfig.model_airmass
    ).fillna(0)
    poa_cal = pvlib.irradiance.get_total_irradiance(
        surface_tilt=surface_tilt,
        surface_azimuth=surface_azimuth,
        solar_zenith=data.zenith,
        solar_azimuth=data.azimuth,
        dni=data.dni,
        ghi=data.ghi,
        dhi=data.dhi,
        dni_extra=dni_extra,
        airmass=air_mass,
        albedo=pvlibconfig.albedo,
        surface_type=pvlibconfig.surface_type,
        model=pvlibconfig.model,
        model_perez=pvlibconfig.model_perez,
    )
    return datetime_or_doy, surface_tilt, surface_azimuth, poa_cal.poa_global.mean()


def daily_poa(args):
    data: pd.DataFrame = args[0]
    surface_tilt: float = args[1]
    surface_azimuth: float = args[2]
    pvlibconfig: PVLIBCONFIG = args[3]
    datetime_or_doy = np.unique(data.index.date)[0]
    dni_extra = pvlib.irradiance.get_extra_radiation(
        datetime_or_doy=datetime_or_doy,
        solar_constant=pvlibconfig.solar_constant,
        method=pvlibconfig.method,
        epoch_year=datetime_or_doy.year,
    )
    air_mass = pvlib.atmosphere.get_relative_airmass(
        zenith=data.zenith, model=pvlibconfig.model_airmass
    ).fillna(0)
    poa_cal = pvlib.irradiance.get_total_irradiance(
        surface_tilt=surface_tilt,
        surface_azimuth=surface_azimuth,
        solar_zenith=data.zenith,
        solar_azimuth=data.azimuth,
        dni=data.dni,
        ghi=data.ghi,
        dhi=data.dhi,
        dni_extra=dni_extra,
        airmass=air_mass,
        albedo=pvlibconfig.albedo,
        surface_type=pvlibconfig.surface_type,
        model=pvlibconfig.model,
        model_perez=pvlibconfig.model_perez,
    )
    return poa_cal.poa_global
