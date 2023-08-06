import plotly.express as px
import numpy as np
import cvxpy as cvx
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from dataclasses import dataclass, asdict
import numpy.typing as npt
from plotly.offline import plot
from plotly.subplots import make_subplots


@dataclass
class SplineFit:
    day: int
    times: list
    measurement: npt.NDArray
    sunny_component: npt.NDArray
    cloud_components: npt.NDArray
    direct_beam_component: npt.NDArray
    diffuse_beam_component: npt.NDArray
    edge_cloud_component: npt.NDArray
    U: npt.NDArray
    U_tilde: npt.NDArray
    soda_fit: pd.DataFrame

    def __post_init__(self):
        # self.measurement += np.random.normal(0, 0.1, size=(self.measurement.shape))
        pass

    @property
    def direct_beam_occlusion(self):
        return self.U @ self.direct_beam_component

    @property
    def diffuse_beam_occlusion(self):
        return self.U @ self.diffuse_beam_component

    @property
    def edge_of_cloud_effect(self):
        return self.U_tilde @ self.edge_cloud_component

    @property
    def total_cloud_attenuation(self):
        return (
            self.direct_beam_occlusion
            + self.diffuse_beam_occlusion
            + self.edge_of_cloud_effect  # Passing negative while creating the instance.
        )

    @property
    def power_estimate(self):
        return abs(
            self.power_scale * self.sunny_component - self.total_cloud_attenuation
        )

    @property
    def power_scale(self):
        return 1

    @property
    def DataFrame(self):
        fitDict = asdict(self)
        fitDict.pop("U", None)
        fitDict.pop("U_tilde", None)
        fitDict.pop("day", None)
        fitDict.pop("times", None)
        fitDict.pop("soda_fit", None)
        fitDict["power_estimate"] = self.power_estimate
        fitDF = pd.DataFrame({k: list(v.flatten()) for k, v in fitDict.items()})
        fitDF.index = (
            self.times
        )  # [f"{self.day} {w:02.0f}:{(60*(w % 1)):02.0f}:00" for w in self.times]
        fitDF.index.name = "time"
        # fitDF.index = pd.to_datetime(fitDF.index)
        # fitDF = fitDF.sort_index()
        return fitDF

    @property
    def NMSE(self):
        return (
            np.linalg.norm(self.measurement - self.power_estimate)
            / np.linalg.norm(self.measurement)
        ) ** 2

    def plot_modeling_fit(self):
        fig = px.line(
            self.DataFrame,
            y=["measurement", "sunny_component", "power_estimate"],
            labels={"value": "Power (kW)"},
        ).update_traces(selector={"name": "measurement"}, line={"dash": "dot"})
        soda_plot = px.line(
            self.soda_fit,
            y="generation",
            x=self.soda_fit.index.hour + self.soda_fit.index.minute / 60 + 1,
        ).update_traces(line_color="yellow")
        fig.add_trace(soda_plot.data[0])
        return fig

    def plot_attenuation_components(self):
        fig = px.line(
            self.DataFrame,
            y=[
                "direct_beam_component",
                "diffuse_beam_component",
                "edge_cloud_component",
            ],
            labels={"value": "Amplitude"},
        )
        return fig

    def plot(self):
        figures = [self.plot_modeling_fit(), self.plot_attenuation_components()]

        fig = make_subplots(
            rows=1,
            cols=len(figures),
            subplot_titles=("Modeling Fit", "Attenuation Components"),
        ).update_layout(title=f"{self.day}")

        for i, figure in enumerate(figures):
            for trace in range(len(figure["data"])):
                fig.append_trace(figure["data"][trace], row=1, col=i + 1)
        fig["layout"]["xaxis"]["title"] = "time of day (hours)"
        fig["layout"]["xaxis2"]["title"] = "time of day (hours)"
        fig["layout"]["yaxis"]["title"] = "Power (kW)"
        fig["layout"]["yaxis2"]["title"] = "Amplitude"
        return fig
