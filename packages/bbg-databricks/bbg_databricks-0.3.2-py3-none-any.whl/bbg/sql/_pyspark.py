import json
import sys
from dataclasses import dataclass, replace
from typing import Any

if sys.version_info < (3, 9):
    from typing import Dict
else:
    from builtins import dict as Dict

import pandas as pd
import pyspark.sql

from bbg._globals import get_global
from ._typing import Connection

spark: pyspark.sql.SparkSession = get_global("spark")

def with_quotes(s: str) -> str:
    """
    Adds double quotes if the string is a single name.
    """
    s = s.strip()
    if len(s) > 0 and s[0].isalpha() and all(
        c.isalnum() or c in "_:" for c in s
    ):
        return json.dumps(s)
    return s


@dataclass
class PySparkQuery(Connection):
    """Helper class for creating queries."""
    _connection: "PySparkConnection"
    _query: str

    def execute(self) -> pd.DataFrame:
        return self._connection.query(self.text())

    def from_table(self, *args: str) -> "PySparkQuery":
        return replace(
            self,
            _query=
                self._query
                + "\nfrom\n    "
                + ".".join(map(with_quotes, args)),
        )

    def group_by(self, *args: str) -> "PySparkQuery":
        return replace(
            self,
            _query=
                self._query
                + "\ngroup by\n    "
                + ",\n    ".join(map(with_quotes, args)),
        )

    def having(self, *args: str, **kwargs: Any) -> "PySparkQuery":
        filters = "\n    and ".join([
            *args,
            *[
                f"{json.dumps(key)} = {repr(value)}"
                for key, value in kwargs.items()
            ],
        ])
        return replace(
            self,
            _query=
                self._query
                + "\nhaving\n    "
                + filters,
        )

    def order_by(self, *args: str) -> "PySparkQuery":
        return replace(
            self,
            _query=
                self._query
                + "\norder by\n    "
                + ",\n    ".join(map(with_quotes, args)),
        )

    def text(self) -> str:
        return self._query

    def where(self, *args: str, **kwargs: Any) -> "PySparkQuery":
        filters = "\n    and ".join([
            *args,
            *[
                f"{json.dumps(key)} = {repr(value)}"
                for key, value in kwargs.items()
            ],
        ])
        return replace(
            self,
            _query=
                self._query
                + "\nwhere\n    "
                + filters,
        )


@dataclass
class PySparkConnection(Connection):
    """
    Base class for PySpark connections to SQL databases using jdbc.
    """
    url: str
    properties: Dict[str, str]

    def query_pyspark(self, query: str) -> pyspark.sql.DataFrame:
        """
        Query the PySpark connection and cache any missing metadata
        from the Azure key vault if missing. This requires the dbutils
        global variable to be set before running.

        Parameters:
            query:
                A SQL table query.

        Returns:
            df:
                A Pandas DataFrame.

        Example:
            >>> query = '''(
            ...     select
            ...         COUNT(DISTINCT "OrderID")
            ...     from
            ...         "SUPPLYCHAIN"."csg.Models.SupplyChain.Data::SalesOrders"
            ... )'''
            >>> df = connection.query(query)
        """
        return spark.read.jdbc(
            self.url, properties=self.properties, table=query
        )

    def query(self, query: str) -> pd.DataFrame:
        """
        Query the PySpark connection and cache any missing metadata
        from the Azure key vault if missing. This requires the dbutils
        global variable to be set before running.

        Parameters:
            query:
                A SQL table query.

        Returns:
            df:
                A Pandas DataFrame.

        Example:
            >>> query = '''(
            ...     select
            ...         COUNT(DISTINCT "OrderID")
            ...     from
            ...         "SUPPLYCHAIN"."csg.Models.SupplyChain.Data::SalesOrders"
            ... )'''
            >>> df = connection.query(query)
        """
        return self.query_pyspark(query).toPandas()

    def select(self, *args: str, **kwargs: Any) -> PySparkQuery:
        return PySparkQuery(
            self,
            "select\n    "
            + ",\n    ".join([
                *map(with_quotes, args),
                *[
                    f"{json.dumps(value)} as {json.dumps(key)}"
                    for key, value in kwargs.items()
                ],
            ]),
        )


def count_of(connection: Connection, query: str) -> int:
    """
    TODO: Add documentation here.
    """
    for count in connection.query(query)["count"]:
        return int(count)
    raise ValueError("empty table, no results")
