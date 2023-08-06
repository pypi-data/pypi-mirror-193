import pandas as pd
import sqlalchemy
from typing import Optional
import pydantic
import dataclasses
from pandas_dataclasses import AsFrame, Data, Index


# @dataclasses.dataclass
# class SolarDataClass:
#     """A dataclass to hold the solar data for a given system.

#     Args:
#         system_id (int): The id of the system.
#         zipcode (str): The zipcode of the system.
#     """

#     datetime: Index[]
#     W: pd.Series


# @pydantic.dataclasses.dataclass
# class LocationDataClass:
#     """A dataclass to hold the location data for a given system.

#     Args:
#         system_id (int): The id of the system.
#         zipcode (str): The zipcode of the system.
#     """

#     solar: pd.DataFrame
#     latitude: float
#     longitude: float
#     info: dict


def get_data(
    engine: sqlalchemy.engine.base.Engine,
    system_id: str,
    year: Optional[str] = None,
    shift: int = 4,
) -> tuple[pd.DataFrame, float, float, str]:
    """Get the solar irradiation data for a given system in the given year.

    Args:
        engine (sqlalchemy.engine.base.Engine): The sqlalchemy engine object for the database to query.
        system_id (str): The id of the system whose data will be returned.
        year (Optional[str]): The year of the solar radiation data to be returned. Defaults to None.
        shift (int): The amount by which to shift the solar radiation data in time. Useful for data with wrong time zone.

    Returns:
        tuple[pd.DataFrame, float, float, str]: The solar radiation data with the latitude, longitude and other metadata about the system.
    """
    solar = (
        pd.DataFrame(
            engine.connect().execute(
                sqlalchemy.text(
                    f"""select * from public.solar where system_id = {system_id};"""
                )
            )
        )
        .sort_values("datetime")
        .loc[:, ["datetime", "kW"]]
        .set_index("datetime")
        .fillna(0)
    )
    solar["kW"] = solar["kW"].values * 1000
    solar = solar.rename(columns={"kW": "W"})
    solar.index = pd.to_datetime(solar.index, utc=True).tz_convert(
        "America/Los_Angeles"
    )
    if year:
        solar = solar.loc[year]

    installation = pd.DataFrame(
        engine.connect().execute(
            sqlalchemy.text(
                f"""select latitude, longitude, arrays from public.installations where system_id = {system_id};"""
            )
        )
    )
    return (
        solar,
        installation.latitude.values[0],
        installation.longitude.values[0],
        installation.arrays.values[0]
        .replace('""', '"')
        .replace("[", "")
        .replace("]", "")[1:-1],
    )


def available_years(
    engine: sqlalchemy.engine.base.Engine,
    system_id: int,
) -> list[str]:
    """Returns a list of available years for a given system.

    Args:
        engine (sqlalchemy.engine.base.Engine): The sqlalchemy engine object for the database to query.
        system_id (str): The id of the system whose available years will be returned.

    Returns:
        list[str]: The list of available years in the dataset.
    """
    solar = (
        pd.read_sql_query(
            f"""select * from public.solar where system_id = {system_id};""", con=engine
        )
        .sort_values("datetime")
        .loc[:, ["datetime", "kW"]]
        .set_index("datetime")
        .fillna(0)
    )
    solar.index = pd.to_datetime(solar.index, utc=True).tz_convert(
        "America/Los_Angeles"
    )
    solar_years = solar.groupby(solar.index.year).count()

    return solar_years.loc[solar_years.kW.isin([8760, 8784])].index.tolist()
