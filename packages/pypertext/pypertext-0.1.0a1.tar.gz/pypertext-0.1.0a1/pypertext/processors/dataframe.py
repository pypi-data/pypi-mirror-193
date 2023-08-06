# Copyright (c) Asif Rahman. (2021-2023)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import typing as t
import logging
from pypertext.processors.base import BaseProcessor
from pypertext import utils
from pypertext.element import Element
from pypertext.plugins import hookimpl
from pypertext.ht import RecordsTable

log = logging.getLogger(__name__)

# Maximum number of rows to request from an unevaluated (out-of-core) dataframe
MAX_UNEVALUATED_DF_ROWS = 10000

_PANDAS_DF_TYPE_STR = "pandas.core.frame.DataFrame"
_PANDAS_INDEX_TYPE_STR = "pandas.core.indexes.base.Index"
_PANDAS_SERIES_TYPE_STR = "pandas.core.series.Series"
_PANDAS_STYLER_TYPE_STR = "pandas.io.formats.style.Styler"
_NUMPY_ARRAY_TYPE_STR = "numpy.ndarray"
_PYSPARK_DF_TYPE_STR = "pyspark.sql.dataframe.DataFrame"
_POLARS_DF_TYPE_STR = "polars.internals.dataframe.frame.DataFrame"
_POLARS_LAZY_DF_TYPE_STR = "polars.internals.lazyframe.frame.LazyFrame"
_XARRAY_DATASET_TYPE_STR = "xarray.core.dataset.Dataset"
_XARRAY_DATAARRAY_TYPE_STR = "xarray.core.dataarray.DataArray"
_PYARROW_TABLE_TYPE_STR = "pyarrow.lib.Table"

_DATAFRAME_LIKE_TYPES = (
    _PANDAS_DF_TYPE_STR,
    _PANDAS_INDEX_TYPE_STR,
    _PANDAS_SERIES_TYPE_STR,
    _PANDAS_STYLER_TYPE_STR,
    _NUMPY_ARRAY_TYPE_STR,
    _POLARS_DF_TYPE_STR,
    _POLARS_LAZY_DF_TYPE_STR,
)


def coerce_to_dataframe(
    df: t.Any, max_unevaluated_rows: int = MAX_UNEVALUATED_DF_ROWS
) -> t.Any:
    """Try to convert different formats to a Pandas Dataframe.

    Args:
        df (ndarray, Iterable, dict, DataFrame, Styler, pa.Table, None, dict, list, or any): DataFrame
        max_unevaluated_rows (int): If unevaluated data is detected this func will evaluate it,
            taking max_unevaluated_rows, defaults to 10k

    Returns:
        (pandas.DataFrame): DataFrame

    Raises:
        (Exception): If the input is not a dataframe-like type
    """
    if utils.is_type(df, _PYARROW_TABLE_TYPE_STR):
        return df.to_pandas()

    if utils.is_type(df, _POLARS_DF_TYPE_STR):
        return df[:max_unevaluated_rows].to_pandas()

    if utils.is_type(df, _POLARS_LAZY_DF_TYPE_STR):
        return df[:max_unevaluated_rows].collect().to_pandas()

    if utils.is_type(df, _PANDAS_DF_TYPE_STR):
        return df

    import pandas as pd

    if utils.is_type(df, _NUMPY_ARRAY_TYPE_STR) and len(df.shape) == 0:
        return pd.DataFrame([])

    if utils.is_type(df, _PYSPARK_DF_TYPE_STR):
        if utils.is_type(df, _PYSPARK_DF_TYPE_STR):
            df = df.limit(max_unevaluated_rows).toPandas()
        else:
            df = pd.DataFrame(df.take(max_unevaluated_rows))
        if df.shape[0] == max_unevaluated_rows:
            log.debug(
                f"⚠️ Showing only {max_unevaluated_rows} rows. "
                "Call `collect()` on the dataframe to show more."
            )
        return df

    # Try to convert to pandas.DataFrame. This will raise an error is df is not
    # compatible with the pandas.DataFrame constructor.
    try:
        return pd.DataFrame(df)
    except ValueError:
        raise Exception(
            f"Unable to convert object of type {type(df)} to `pandas.DataFrame`."
        )


class DataFrameProcessor(BaseProcessor):
    """Processor for Pandas or Polars dataframes."""

    @classmethod
    def is_valid_type(cls, data) -> bool:
        return any([utils.is_type(data, t) for t in _DATAFRAME_LIKE_TYPES])

    def get_element(self) -> Element:
        df = coerce_to_dataframe(self.data)
        records = df.to_dict(orient="records")
        el = RecordsTable(id=self.key).from_records(records)
        return el


@hookimpl
def register_processor_classes():
    return DataFrameProcessor
