from typing import Literal
import sqlalchemy
import json
from CEDSSolar.gridSearch.query import get_data
from CEDSSolar.gridSearch.GridSearchKevala import SolarPVMetaData
from CEDSSolar.gridSearch.fit import Fit
import numpy as np
from CEDSSolar.gridSearch.DPBayesOpt import DPBayesOpt
import matplotlib.pyplot as plt
import argparse
import pandas as pd


class DPInfer:
    """This class is used to infer the surface azimuth and tilt of a solar PV system.

    Args:
        psql_config (argparse.Namespace): The configuration for the PostgreSQL database.
        system_id (str): The system ID of the solar PV system.
        year (str): The year's data to use for inference.
    """

    def __init__(self, psql_config: argparse.Namespace, system_id: str, year: str):
        self.psql_config = psql_config
        self.system_id = system_id
        self.year = year
        self.ingest_data()
        self.has_optimized = False

    def ingest_data(self) -> None:
        """This method ingests the data from the PostgreSQL database and creates the SolarPVMetaData object."""
        engine = sqlalchemy.create_engine(
            f"postgresql://{self.psql_config.username}:{self.psql_config.password}@{self.psql_config.host}:{self.psql_config.port}/{self.psql_config.dbname}"
        )
        df, lat, lon, info = get_data(engine, self.system_id, self.year)
        self.smd = SolarPVMetaData(df.copy(), lat=lat, lon=lon, year=self.year)
        self.true_fit = Fit(json.loads(info)["azimuth"], 90)

    def black_box_function(
        self, surface_azimuth: float, surface_tilt: float, noise: float = 0.1
    ) -> float:
        """This method is the black box function to be optimized.

        Args:
            surface_azimuth (float): The surface azimuth of the solar PV system.
            surface_tilt (float): The surface tilt of the solar PV system.
            noise (float, optional): The noise to add to the function evaluation. Defaults to 0.1.

        Returns:
            float: The function evaluation at the given surface azimuth and tilt.
        """
        return self.smd.black_box_function(
            surface_azimuth=int(surface_azimuth), surface_tilt=int(surface_tilt)
        ) + np.random.normal(loc=0, scale=noise)

    def optimize(
        self,
        iterations: int = 90,
        init_points: int = 100,
        n_iter: int = 0,
        verbose: Literal[0, 1, 2] = 1,
    ):
        """This method runs the optimization.

        Args:
            iterations (int, optional): The number of optimization iterations to run. Defaults to 90.
            init_points (int, optional): Number of iterations before the explorations starts the exploration for the maximum. Defaults to 100.
            n_iter (int, optional): Number of iterations where the method attempts to find the maximum
            value. Defaults to 0.
            verbose (Literal[0, 1, 2], optional): The verbosity of the optimizer. Choose 0 to silence the outputs. Choose 1 to print only when a maximum is observed. Choose 2 to print the output at each iteration. Defaults to 1.
        """
        self.optimizer = DPBayesOpt(
            f=self.black_box_function, verbose=verbose, iterations=iterations
        )
        self.optimizer.optimize(**dict(init_points=init_points, n_iter=n_iter))
        self.has_optimized = True

    def plot(self):
        """This method plots the optimization results."""
        if not self.has_optimized:
            raise ValueError("You must run optimize() before plotting.")
        self.optimizer.plot()
        plt.show()

    @property
    def best_params(self) -> dict:
        """This method returns the best parameters found by the optimizer.

        Raises:
            ValueError: When the optimize method has not been run.

        Returns:
            dict: The best parameters found by the optimizer.
        """
        if not self.has_optimized:
            raise ValueError("You must run optimize() before plotting.")
        return self.optimizer.optimizer.max

    def infer(self, n_samples: int = 1000, infer_epsilon: float = 100) -> pd.Series:
        """This method infers the posterior distribution of the surface azimuth and tilt.

        Args:
            n_samples (int, optional): The number of samples to draw from the posterior distribution. Defaults to 1000.
            infer_epsilon (float, optional): The epsilon value to use for inference. Defaults to 100.

        Raises:
            ValueError: When the optimize method has not been run.

        Returns:
            pd.Series: The inferred DP surface azimuth and tilt pairs.
        """
        if not self.has_optimized:
            raise ValueError("You must run optimize() before plotting.")
        return self.optimizer.infer(n=n_samples, infer_epsilon=infer_epsilon)
