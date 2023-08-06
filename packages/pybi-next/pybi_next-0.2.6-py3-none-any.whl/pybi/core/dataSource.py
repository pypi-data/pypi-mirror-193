from __future__ import annotations
from pybi.utils.data_gen import get_global_id, Jsonable, random_dv_name
import pandas as pd
from enum import Enum
from typing import Dict, List, Any, Callable, Optional, TYPE_CHECKING, Union

from pybi.core.sql import Sql

if TYPE_CHECKING:
    from pybi.app import App


class DataViewType(Enum):
    Sql = "sql"
    Pivot = "pivot"


class DataViewBase(Jsonable):
    def __init__(self, name: str, type: DataViewType) -> None:
        super().__init__()
        self.name = name
        self.type = type
        self.__excludeLinkages: List[str] = []

    def exclude_source(self, name: str):
        self.__excludeLinkages.append(name)
        return self

    def _to_json_dict(self):
        data = super()._to_json_dict()
        data["excludeLinkages"] = self.__excludeLinkages
        return data


class DataView(DataViewBase):
    def __init__(self, name: str, sql: Sql) -> None:
        super().__init__(name, DataViewType.Sql)
        self._sql = sql

    def _to_json_dict(self):
        data = super()._to_json_dict()
        data["sql"] = self._sql.sql
        return data


class PivotDataView(DataViewBase):
    def __init__(
        self,
        name: str,
        source: str,
        row: str,
        column: str,
        cell: str,
        agg="min",
    ) -> None:
        super().__init__(name, DataViewType.Pivot)
        self.source = source
        self._row = row
        self._column = column
        self._cell = cell
        self._agg = agg

    def _to_json_dict(self):
        data = super()._to_json_dict()
        data["pivotOptions"] = {
            "row": self._row,
            "column": self._column,
            "cell": self._cell,
            "agg": self._agg,
        }
        return data


class DataSource(Jsonable):
    def __init__(self, name: str, data: pd.DataFrame) -> None:
        super().__init__()
        self._data = data
        self.name = name

    def __str__(self) -> str:
        return self.name


class DataSourceView:
    def __init__(self) -> None:
        pass

    def _to_sql(self):
        raise NotImplementedError()


class DataSourceField(DataSourceView):
    def __init__(self, source_name: str, name: str) -> None:
        super().__init__()
        self.source_name = source_name
        self.name = name

    def __str__(self) -> str:
        return str(Sql(self._to_sql()))

    def _to_sql(self):
        return f"select {self.name} from {self.source_name}"


class PyechartsPieItem(DataSourceView):
    def __init__(self, ds_table: DataSourceTable) -> None:
        super().__init__()
        self.ds_table = ds_table

    def __getitem__(self, key):
        from pyecharts import options as opts

        if key > 0:
            raise StopIteration()

        return opts.PieItem("", 0)

    def _to_sql(self):

        if len(self.ds_table.columns) < 2:
            raise Exception("pie data must have 2 fields")

        name = f"{self.ds_table.columns[0]} as name"
        value = f"{self.ds_table.columns[1]} as value"

        return f"select {name} , {value} from ({self.ds_table._to_sql()})"


class PyechartsLineItem(DataSourceView):
    def __init__(self, ds_table: DataSourceTable) -> None:
        super().__init__()
        self.ds_table = ds_table

    def __getitem__(self, key):
        from pyecharts import options as opts

        if key > 0:
            raise StopIteration()

        return opts.LineItem("", 0)

    def _to_sql(self):

        if len(self.ds_table.columns) < 3:
            raise Exception("pie data must have 3 fields")

        series_name = f"{self.ds_table.columns[0]} as sreies"
        name = f"{self.ds_table.columns[1]} as name"
        value = f"{self.ds_table.columns[2]} as value"

        return f"select {series_name},{name} , {value} from ({self.ds_table._to_sql()})"


class DataSourceTable(DataSourceView):
    def __init__(
        self,
        source_name: str,
        columns: List[str],
        *,
        host: App,
    ) -> None:
        super().__init__()
        self.source_name = source_name
        self.columns = columns
        self.__host = host

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration

    def __getitem__(self, field: Union[str, List[str]]):
        if isinstance(field, str):
            return DataSourceField(self.source_name, field)
        return DataSourceTable(self.source_name, field, host=self.__host)

    def to_pivot(
        self,
        row: str,
        column: str,
        cell: str,
        agg="min",
        exclude_source: Optional[List[DataSourceTable]] = None,
    ):
        """
        agg : sqlite aggregate function,like 'min','max','sum','round(avg(${}),2)'
            default:'min'
        """
        return self.__host.set_pivot_dataView(
            self.source_name, row, column, cell, agg, exclude_source
        )

    def to_pyecharts_pie_items(self) -> Any:
        return PyechartsPieItem(self)

    def to_pyecharts_line_items(self) -> Any:
        return PyechartsLineItem(self)

    def get_sql_fields(self):
        """
        >>> *
        >>> a,b,c
        """
        return "*" if len(self.columns) == 0 else ",".join(self.columns)

    def _to_sql(self):
        fields = self.get_sql_fields()

        return f"select {fields} from {self.source_name}"

    def __str__(self) -> str:
        return self.source_name
