from scipy.interpolate import CubicHermiteSpline
import pandas as pd
import numpy as np
import plotly.graph_objects as go


class CHS:
    def __init__(self, data: pd.DataFrame, col: str = "W") -> None:
        self.data = data
        self.col = col
        self.original_data = self.data.copy()
        self._clean_data()
        self._get_daylight_data()
        self._get_derivative_via_neighbors()
        self._CubicHermiteSpline()

    def _clean_data(self) -> None:
        """Make all power generations below 0 equal to 0."""
        self.data.loc[self.data[self.col] <= 0] = 0

    def _get_daylight_data(self) -> None:
        """Get daylight data where solar power generation is above 0."""
        self.daylight = self.data.loc[self.data[self.col] > 0]
        self.samplingPeriod = 1
        self.daylightDuration = len(self.daylight)
        self.N = int(self.daylightDuration / (2 * self.samplingPeriod))
        self.daylight_values = self.daylight.values.flatten().tolist()
        if self.daylightDuration % 2 == 0:
            correction = 0
        else:
            correction = 1
        self.daylight_x = np.arange(-self.N, self.N + correction).tolist()

    def _get_derivative_via_neighbors(self) -> None:
        """Approximate the derivatives at each point using the neighboring values."""
        self.derivative = [0] * self.daylightDuration
        for i in range(self.daylightDuration):
            if i == 0:
                self.derivative[i] = (
                    self.daylight_values[i + 1] - self.daylight_values[i]
                )
            elif 1 <= i < self.daylightDuration - 1:
                self.derivative[i] = (
                    self.daylight_values[i + 1] - self.daylight_values[i - 1]
                ) / 2
            else:
                self.derivative[i] = (
                    self.daylight_values[i] - self.daylight_values[i - 1]
                )

    def _CubicHermiteSpline(self) -> None:
        self.spline = CubicHermiteSpline(
            self.daylight_x, self.daylight_values, self.derivative
        )

    def generate_Spline(
        self,
        x_index: list[float],
        x_DateTimeIndex: list[pd.Timestamp],
        plot_spline: bool = False,
    ):
        y = self.spline(x_index)
        if plot_spline:
            return y, self.plot_spline(x_DateTimeIndex, y)
        return y

    def plot_spline(self, x: list[float], y: list[float]):
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                name="spline",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=self.daylight.index.values.flatten(),
                y=self.daylight_values,
                name="Solar Generation",
                mode="markers",
                marker={"size": 3},
            )
        )
        return fig
