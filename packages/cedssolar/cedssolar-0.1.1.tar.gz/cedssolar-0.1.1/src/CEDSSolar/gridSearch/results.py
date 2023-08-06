import numpy as np
import pandas as pd
from pandas_dataclasses import AsDataFrame, Data, Index
from dataclasses import dataclass


@dataclass
class GridSearchResults(AsDataFrame):
    """A dataclass for the grid search results dataframe.

    Args:
        surface_azimuth (Index[float]): The azimuth.
        surface_tilt (Index[float]): The tilt.
        RMSE (Index[float]): The RMSE of the fit.
        MAE (Index[float]): The MAE of the fit.
    """

    surface_azimuth: Index[float]
    surface_tilt: Index[float]
    RMSE: Data[float]
    MAE: Data[float]


def filter_grid_search_results(
    results: list[GridSearchResults], top_percent_to_retain_per_month: float = 0.01
) -> list[GridSearchResults]:
    """Return only the top rows with the smallest RMSE in each GridSearchResults/

    Args:
        results (list[GridSearchResults]): The list grid search fit results.
        top_percent_to_retain_per_month (float, optional): The percent of rows to retain. Defaults to 0.01.

    Returns:
        list[GridSearchResults]: _description_
    """
    results_filt = list()
    for result in results:
        results_filt.append(
            result.nsmallest(
                int(np.ceil(top_percent_to_retain_per_month * len(result))),
                "RMSE",
                keep="all",
            )
        )
    return results_filt


def aggregate_across_months(
    monthly_results: list[GridSearchResults],
    top_percent_to_retain_per_month: float = 0.01,
    rmse_filtered: bool = True,
) -> pd.DataFrame:
    """_summary_

    Args:
        monthly_results (list[GridSearchResults]): _description_
        top_percent_to_retain_per_month (float, optional): _description_. Defaults to 0.01.
        rmse_filtered (bool, optional): _description_. Defaults to True.

    Returns:
        pd.DataFrame: _description_
    """
    results_filt = list()
    for result in monthly_results:
        results_filt.append(
            result.nsmallest(
                int(np.ceil(top_percent_to_retain_per_month * len(result))),
                "RMSE",
                keep="all",
            )
        )
    yearly_results_filtered = pd.concat(results_filt, axis=0)
    yearly_results_unfiltered = pd.concat(monthly_results, axis=0)
    # Aggregating RMSE and MAE
    if rmse_filtered:
        yearly_results_elastic = yearly_results_filtered.groupby(
            ["surface_azimuth", "surface_tilt"]
        ).agg({"RMSE": "mean", "MAE": "mean"})
    else:
        yearly_results_elastic = yearly_results_unfiltered.groupby(
            ["surface_azimuth", "surface_tilt"]
        ).agg({"RMSE": "mean", "MAE": "mean"})
    # Aggregating counts
    yearly_results_count = yearly_results_filtered.value_counts(
        ["surface_azimuth", "surface_tilt"]
    ).to_frame("count")
    yearly_results = pd.concat([yearly_results_elastic, yearly_results_count], axis=1)
    return yearly_results
