from enum import Enum
from typing import Any, Optional

import pandas as pd
import pyspark.sql

from bbg.secrets import Client
from ._typing import Connection
from ._pyspark import PySparkConnection, PySparkQuery


class Hana(Connection, Enum):
    """The Hana SQL connection with known source and driver."""
    _connection: Optional[PySparkConnection]

    CONNECTION = None

    def __init__(self, value: None) -> None:
        self._connection = None

    def _clean(self, query: str) -> str:
        """Cleans a query by adding parentheses."""
        query = super()._clean(query)
        if not query.startswith("("):
            query = "(" + query
        if query.count(")") < query.count("("):
            query += ")"
        return query

    def _ensure_connection(self) -> PySparkConnection:
        if self._connection is not None:
            return self._connection
        with Client.connect() as client:
            username, password, hostname, port = [
                client.get_secret(f"HANASidecarOnPrem{key}")
                for key in ("User", "Secret", "IP", "Port")
            ]
        url = f"jdbc:sap://{hostname}:{port}"
        properties = {
            "user": username,
            "password": password,
            "driver": "com.sap.db.jdbc.Driver",
        }
        connection = PySparkConnection(url, properties)
        self._connection = connection
        return connection

    def query_pyspark(self, query: str) -> pyspark.sql.DataFrame:
        """
        Query the Hana connection and cache any missing metadata from
        the Azure key vault if missing. This requires the dbutils
        global variable to be set before running.

        Parameters:
            query:
                A SQL table query.

        Returns:
            df:
                A PySpark DataFrame.

        Example:
            >>> query = '''
            ...     select
            ...         COUNT(DISTINCT "OrderID")
            ...     from
            ...         "SUPPLYCHAIN"."csg.Models.SupplyChain.Data::SalesOrders"
            ... '''
            >>> df = connection.query(query)
        """
        return self._ensure_connection().query_pyspark(self._clean(query))

    def query(self, query: str) -> pd.DataFrame:
        """
        Query the Hana connection and cache any missing metadata from
        the Azure key vault if missing. This requires the dbutils
        global variable to be set before running.

        Parameters:
            query:
                A SQL table query.

        Returns:
            df:
                A Pandas DataFrame.

        Example:
            >>> query = '''
            ...     select
            ...         COUNT(DISTINCT "OrderID")
            ...     from
            ...         "SUPPLYCHAIN"."csg.Models.SupplyChain.Data::SalesOrders"
            ... '''
            >>> df = connection.query(query)
        """
        return self._ensure_connection().query(self._clean(query))

    def select(self, *args: str, **kwargs: Any) -> PySparkQuery:
        return self._ensure_connection().select(*args, **kwargs)


hana = Hana.CONNECTION
