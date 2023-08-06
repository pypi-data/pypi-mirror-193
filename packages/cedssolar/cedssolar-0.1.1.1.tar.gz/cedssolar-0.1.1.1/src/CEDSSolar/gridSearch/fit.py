from dataclasses import dataclass
from typing import Literal
import numpy as np
import pandas as pd
from .results import GridSearchResults


@dataclass
class Fit:
    """A dataclass for a pair of (azimuth, tilt) fit.

    Args:
        azimuth (float): The azimuth.
        tilt (float): The tilt

    Returns:
        Fit: The fit.
    """

    azimuth: float
    tilt: float

    def __repr__(self) -> str:
        return f"Fit(azimuth:{self.azimuth:0.2f}, tilt:{self.tilt:0.2f})"


def best_fit(
    results: list[GridSearchResults],
    kind: Literal["count", "elastic"] = "count",
    q: float = 0.001,
) -> Fit:
    """Given a list of monthly results, return a pair of (azimuth, tilt) that provides the best fit according
    to either the number of times a pair appears in the monthly results ("count") or the best RMSE + MAE values.

    Args:
        results (list[GridSearchResults]): The list of monthly results.
        kind (Literal[&quot;count&quot;, &quot;elastic&quot;], optional): The criteria by which to find the best fit.
        Defaults to "count".
        q (float, optional): The quantile at which to consider the pairs for the best fir. Defaults to 0.001.

    Raises:
        ValueError: If kind is not "count" or "elastic".

    Returns:
        Fit: The best fit.
    """
    if kind == "count":
        top_results = results.loc[results["count"] == results["count"].max()]
    elif kind == "elastic":
        top_results = results.loc[
            (results.RMSE + results.MAE) < (results.RMSE + results.MAE).quantile(q)
        ]
    else:
        raise ValueError("Should be either 'count' or 'elastic'")

    return Fit(*np.array(top_results.index.values.tolist()).mean(axis=0).tolist())
