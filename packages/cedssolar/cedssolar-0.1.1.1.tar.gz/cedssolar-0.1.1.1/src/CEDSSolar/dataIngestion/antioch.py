from typing import List
import psycopg2
import pandas.io.sql as sqlio
import pandas as pd


class Database:
    def __init__(
        self, hostname: str, port: int, dbname: str, username: str, password: str
    ) -> None:
        self.hostname = hostname
        self.port = port
        self.dbname = dbname
        self.username = username
        self.password = password

        self.connection = psycopg2.connect(
            f"""
                dbname={self.dbname} 
                user={self.username} 
                password={self.password} 
                host={self.hostname} 
                port={self.port}
            """
        )

    def get_generation_data_for_zipcode(self, zipcode: List[str]) -> pd.DataFrame:
        """_summary_

        Args:
            zipcode (List[str]): The zipcode to get generation data for.

        Returns:
            pd.DataFrame: The solar generation data for the given zipcode.
        """
        sql = f"select * from public.location where zip in {zipcode};"
        return sqlio.read_sql_query(sql, self.connection)
