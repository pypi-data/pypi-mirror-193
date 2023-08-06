"""
    This module provides all backend code.
    Based on FastAPI
"""

import os
from pathlib import Path
from typing import Union, Optional

import pandas as pd

from ..dtypes.typing import ColumnTypeMapping

from .data_source import DataSource
from .pandas_data_source import PandasDataSource
from .hdf5_data_source import Hdf5DataSource
from .exceptions import InvalidPath


def create_datasource(
    source: Union[pd.DataFrame, os.PathLike, str],
    dtype: Optional[ColumnTypeMapping] = None,
) -> DataSource:
    """
    open the specified data source
    """
    if isinstance(source, pd.DataFrame):
        return PandasDataSource(df=source, dtype=dtype)

    if Path(source).suffix == ".csv":
        df = pd.read_csv(source)
        return PandasDataSource(df=df, dtype=dtype)

    if Path(source).suffix == ".h5":
        return Hdf5DataSource(table_file=source)

    raise InvalidPath(source)
