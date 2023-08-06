import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from .fit import Fit
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


def plot_final(
    yearly_results_list: list[pd.DataFrame],
    true_fit: Fit,
    best_fit_list: list[Fit],
    by: str = "count",
    vmax: float = 12,
    vmin: float = 0,
):
    fig, axes = plt.subplots(
        nrows=1,
        ncols=len(yearly_results_list),
        subplot_kw=dict(projection="polar"),
        figsize=(15, 6),
    )
    if len(yearly_results_list) == 1:
        axes = np.array([axes])

    for idx, (yearly_results, best_fit) in enumerate(
        zip(yearly_results_list, best_fit_list)
    ):
        a = np.radians(yearly_results.index.get_level_values("surface_azimuth"))
        b = yearly_results.index.get_level_values("surface_tilt")
        z = yearly_results[by]
        xi = np.linspace(a.min(), a.max(), 100)
        yi = np.linspace(b.min(), b.max(), 100)
        theta, r = np.meshgrid(xi, yi)
        zi = sp.interpolate.griddata((a, b), z, (theta, r), method="linear")

        plt.sca(axes[idx])
        # cset = plt.scatter(theta, r, c=zi, vmin=0, vmax=0.7)
        cset = plt.scatter(theta, r, c=zi, vmin=vmin, vmax=vmax, cmap=plt.cm.jet)
        axes[idx].set_theta_direction(-1)
        axes[idx].set_theta_zero_location("N")
        axes[idx].set_rgrids(np.arange(30, 120, 30))
        axes[idx].set_thetagrids(
            np.arange(0, 360, 45), ("N", "NE", "E", "SE", "S", "SW", "W", "NW")
        )
        axes[idx].tick_params(labelsize=20)
        axes[idx].scatter(x=np.deg2rad(270), y=0, c="black", s=1)
        axes[idx].scatter(
            x=np.deg2rad(true_fit.azimuth),
            y=true_fit.tilt,
            c="black",
            s=100,
            label=f"True {true_fit}",
            marker="*",
        )
        axes[idx].scatter(
            x=np.deg2rad(best_fit.azimuth),
            y=best_fit.tilt,
            c="maroon",
            s=100,
            label=f"Estimated {best_fit}",
            marker="*",
        )
        axes[idx].legend()
    plt.colorbar(ax=axes.tolist(), shrink=0.6)
    plt.show()


def plot_grid_search_results(results: list[pd.DataFrame]):
    fig, axes = plt.subplots(
        nrows=2, ncols=6, subplot_kw=dict(projection="polar"), figsize=(15, 6)
    )
    axes = axes.ravel()
    for month, result in enumerate(results):
        a = np.radians(result["surface_azimuth"])
        b = result["surface_tilt"]
        z = result["MAE"] + result["RMSE"]
        xi = np.linspace(a.min(), a.max(), 100)
        yi = np.linspace(b.min(), b.max(), 100)
        theta, r = np.meshgrid(xi, yi)
        zi = sp.interpolate.griddata((a, b), z, (theta, r), method="linear")

        plt.sca(axes[month])
        cset = plt.scatter(theta, r, c=zi, vmin=0, vmax=0.3)
        axes[month].set_theta_direction(-1)
        axes[month].set_theta_zero_location("N")
        axes[month].set_rgrids(np.arange(30, 120, 30))
        axes[month].set_thetagrids(
            np.arange(0, 360, 45), ("N", "NE", "E", "SE", "S", "SW", "W", "NW")
        )
        axes[month].tick_params(labelsize=6)
        axes[month].title.set_text(
            f"{datetime.strptime(str(month+1), '%m').strftime('%B')}"
        )
    plt.colorbar(ax=axes.tolist(), shrink=0.6)
    plt.show()


def plotly_final(
    results_list: list[pd.DataFrame],
    true_fit: Fit,
    best_fit_list: list[Fit],
    by: str = "count",
    cmax: float = 12,
    cmin: float = 0,
) -> go.Figure:
    """Plot the fit results.

    Args:
        results_list (list[pd.DataFrame]): The list of monthly fit results.
        true_fit (Fit): The true fit for the given data.
        best_fit_list (list[Fit]): The list of best fits for the elements in the results_list.
        by (str, optional): The values to use to plot the propensity of the fit. Defaults to "count".
        cmax (float, optional): The minimum for the colormap. Defaults to 12.
        cmin (float, optional): The maximum for the colormap. Defaults to 0.

    Returns:
        go.Figure: The fit plot.
    """
    fig = make_subplots(
        rows=1,
        cols=len(results_list),
        specs=[[{"type": "polar"}] * len(results_list)],
    )

    for idx, (yearly_results, best_fit) in enumerate(zip(results_list, best_fit_list)):
        a = np.radians(yearly_results.index.get_level_values("surface_azimuth"))
        b = yearly_results.index.get_level_values("surface_tilt")
        z = yearly_results[by]
        xi = np.linspace(a.min(), a.max(), 100)
        yi = np.linspace(b.min(), b.max(), 100)
        theta, r = np.meshgrid(xi, yi)
        zi = sp.interpolate.griddata((a, b), z, (theta, r), method="linear")
        zi_idx = ~np.isnan(zi.flatten())
        r = r.flatten()[zi_idx]
        theta = theta.flatten()[zi_idx]
        zi = zi.flatten()[zi_idx]
        fig.add_trace(
            go.Scatterpolar(
                mode="markers",
                r=r,
                theta=np.rad2deg(theta),
                marker_color=zi,
                marker=dict(
                    cmin=cmin,
                    cmax=cmax,
                    autocolorscale=True,
                    colorscale="Blackbody",
                    showscale=True,
                    coloraxis="coloraxis",
                ),
                legendgroup="Fit strength",
                showlegend=True if idx + 1 == 1 else False,
                hovertext=zi.flatten(),
                subplot=f"polar{idx+1}",
                name=f"Fit strength",
            ),
            row=1,
            col=idx + 1,
        )
        fig.add_trace(
            go.Scatterpolar(
                mode="markers",
                r=[true_fit.tilt],
                theta=[true_fit.azimuth],
                marker=dict(color="green", symbol="star-diamond", size=15),
                legendgroup="true_fit",
                name=f"True Fit",
                showlegend=True if idx + 1 == 1 else False,
            ),
            row=1,
            col=idx + 1,
        )
        fig.add_trace(
            go.Scatterpolar(
                mode="markers",
                r=[best_fit.tilt],
                theta=[best_fit.azimuth],
                marker=dict(color="maroon", symbol="hexagram", size=15),
                legendgroup="best_fit",
                name=f"Best Fit",
                showlegend=True if idx + 1 == 1 else False,
            ),
            row=1,
            col=idx + 1,
        )
    fig.update_layout(
        polar1=dict(
            radialaxis=dict(range=[0, 95]),
            # radialaxis_type="log",
            radialaxis_angle=-45,
            angularaxis=dict(
                direction="clockwise",
                period=6,
                tickvals=[0, 45, 90, 135, 180, 225, 270, 315],
                ticktext=["N", "NE", "E", "SE", "S", "SW", "W", "NW"],
            ),
        ),
        polar2=dict(
            radialaxis=dict(range=[0, 95]),
            # radialaxis_type="log",
            angularaxis=dict(
                direction="clockwise",
                period=6,
                tickvals=[0, 45, 90, 135, 180, 225, 270, 315],
                ticktext=["N", "NE", "E", "SE", "S", "SW", "W", "NW"],
            ),
        ),
    )
    # fig.update_layout(coloraxis_colorbar=dict(yanchor="top", y=1, x=0, ticks="outside"))
    fig.update_layout(legend_orientation="h")
    return fig
