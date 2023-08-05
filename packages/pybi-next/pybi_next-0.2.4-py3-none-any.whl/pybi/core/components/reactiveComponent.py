from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional, Dict, Set, Any, Union

from pybi.utils.data_gen import Jsonable
import pybi.utils.dictUtils as dictUtils

from .componentTag import ComponentTag
from .component import Component
from pybi.core.sql import Sql

from pybi.core.dataSource import DataSourceView, DataSourceField, DataSourceTable
import re


if TYPE_CHECKING:
    from pybi.core.dataSource import DataSourceTable


class UpdateInfo(Jsonable):
    def __init__(self, table: str, field: str) -> None:
        super().__init__()
        self.table = table
        self.field = field


class ReactiveComponent(Component):
    def __init__(self, tag: ComponentTag) -> None:
        super().__init__(tag)
        self._updateInfos: List[UpdateInfo] = []

    def add_updateInfo(self, table: str, field: str):
        self._updateInfos.append(UpdateInfo(table, field))
        return self

    def _to_json_dict(self):
        data = super()._to_json_dict()
        data["updateInfos"] = self._updateInfos

        return data


class SingleReactiveComponent(ReactiveComponent):
    def __init__(self, tag: ComponentTag, sql: Sql) -> None:
        super().__init__(tag)
        self._sql = sql

    def sql(self, sql: str):
        self._sql = sql
        return self

    def _to_json_dict(self):
        data = super()._to_json_dict()
        data["sqlInfo"] = self._sql
        return data


m_sql_from_text_pat = re.compile(r"(?:sql:\[_\s)(.+?)(?:\s_])", re.I)


class TextValue(ReactiveComponent):
    def __init__(self, contexts: List[Union[str, Sql]]) -> None:
        super().__init__(ComponentTag.TextValue)
        self.contexts = contexts

    @staticmethod
    def extract_sql_from_text(text: str):
        """
        >>> input = '总销售额:sql:[_ select sum(销售额) from data _]'
        >>> extract_sql_from_text(input)
        >>> ['总销售额:',Sql('select sum(销售额) from data')]
        """
        start_idx = 0

        for match in re.finditer(m_sql_from_text_pat, text):

            span = match.span()

            if span[0] > start_idx:
                # 前面有普通文本
                yield text[start_idx : span[0]]

            yield Sql(match.group(1))
            start_idx = span[1]

        end_idx = len(text) - 1

        if start_idx < end_idx:
            yield text[start_idx : len(text)]


class Slicer(SingleReactiveComponent):
    def __init__(self, sql: Sql) -> None:
        super().__init__(ComponentTag.Slicer, sql)
        self.title = ""
        self.multiple = True

    def set_title(self, title: str):
        self.title = title
        return self

    def set_multiple(self, multiple: bool):
        self.multiple = multiple
        return self


class Table(SingleReactiveComponent):
    def __init__(
        self,
        sql: Sql,
    ) -> None:
        super().__init__(ComponentTag.Table, sql)


class EChartSqlInfo(Jsonable):
    def __init__(self, seriesConfig: Dict, path: str, sql: Sql, chartType: str) -> None:
        self.path = path
        self._sql = sql
        self.chartType = chartType
        self.seriesConfig = seriesConfig

    def _to_json_dict(self):
        data = super()._to_json_dict()
        sql_data = self._sql._to_json_dict()

        data = {**data, **sql_data}
        return data


class EChartUpdateInfo(Jsonable):
    def __init__(
        self,
        action_type: str,
        value_type: str,
        table: str,
        field: str,
    ) -> None:
        """
        action_type : Literal["hover", "click"]
        value_type: Literal["x", "y", "value"]
        """
        super().__init__()
        self.actionType = action_type
        self.valueType = value_type
        self.table = table
        self.field = field


class EChart(ReactiveComponent):
    def __init__(self, options: Dict) -> None:

        super().__init__(ComponentTag.EChart)

        self._chart_mappings = {}
        self.options = options
        self._sqlInfos: List[EChartSqlInfo] = []
        self._chartUpdateInfos: List[EChartUpdateInfo] = []
        self.height = "30em"

    def set_height(self, value: str):
        """
        15em:15字体大小
        300px:300像素
        """
        self.height = value
        return self

    def add_sql_path(self, info: EChartSqlInfo):
        """
        add_sql_path('xAxis.data',"select distinct name from data")
        """
        self._sqlInfos.append(info)
        return self

    def hover_filter(
        self, value_type: str, table: Union[str, DataSourceTable], field: str
    ):
        """
        value_type: Literal["x", "y", "value"]
        """
        if isinstance(table, DataSourceTable):
            table = table.source_name

        self._chartUpdateInfos.append(
            EChartUpdateInfo("hover", value_type, table, field)
        )
        return self

    def _to_json_dict(self):

        EChart.remove_sql_from_option(self.options, self._sqlInfos)
        EChart.remove_legend_empty_data(self.options)

        data = super()._to_json_dict()
        data["mapping"] = self._chart_mappings

        data["sqlInfos"] = self._sqlInfos
        data["updateInfos"] = self._chartUpdateInfos

        return data

    @staticmethod
    def remove_legend_empty_data(options: Dict):
        target = options
        if "legend" in target:
            target = options["legend"]
            if isinstance(target, list):
                target = target[0]
                if (
                    "data" in target
                    and isinstance(target["data"], list)
                    and len(target["data"]) == 0
                ):
                    target["data"] = None

    @staticmethod
    def extract_infos_from_option(opt: Dict):

        yield from EChart._extract_series_infos_from_option_(opt)
        return
        stack = [("", opt)]

        while len(stack) > 0:

            path, target = stack.pop()

            for key, value in target.items():
                if key != "series":
                    cur_path = f"{path}.{key}"

                    if isinstance(value, dict):
                        stack.append((cur_path, value))
                    elif isinstance(value, list):
                        for idx, v in enumerate(value):
                            if isinstance(v, dict):
                                stack.append((f"{cur_path}[{idx}]", v))
                    elif isinstance(value, (Sql, DataSourceView)):

                        if isinstance(value, DataSourceView):
                            value = Sql(value._to_sql())

                        yield EChartSqlInfo(cur_path[1:], value, "other")

    @staticmethod
    def _extract_series_infos_from_option_(opt: Dict):
        if "series" not in opt:
            return

        def extract_series(series: Dict, idx=-1):
            series_data = series["data"]
            if series["type"] in ["line", "pie", "bar"]:
                if isinstance(series_data, (Sql, DataSourceView)):
                    if isinstance(series_data, DataSourceView):
                        series_data = Sql(series_data._to_sql())

                    path = "series"
                    if idx > -1:
                        path = f"{path}[{idx}].data"

                    series["pybiFlag"] = None

                    yield EChartSqlInfo(series, path, series_data, series["type"])

        series = opt["series"]
        if isinstance(series, list):
            for idx, s in enumerate(series):
                yield from extract_series(s, idx)
        else:
            yield from extract_series(series)

    @staticmethod
    def remove_sql_from_option(opt: Dict, infos: List[EChartSqlInfo]):

        filterSeries = [series for series in opt["series"] if not "pybiFlag" in series]

        opt["series"] = filterSeries

        # for info in infos:
        #     paths = info.path.split(".")
        #     dictUtils.set_by_paths(paths, opt, None)
