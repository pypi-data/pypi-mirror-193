from __future__ import annotations
from pybi.utils.data_gen import Jsonable, get_global_id
from typing import List, TYPE_CHECKING, Optional, Any
from .statementsTag import StatementType


if TYPE_CHECKING:
    from pybi.app import App
    from pybi.core.components import ReactiveComponent


class Statement(Jsonable):
    def __init__(self, type: StatementType) -> None:
        self.id = get_global_id()
        self.type = type
        self.children: List[Statement] = []

    def _add_statement(self, stat: Statement):
        self.children.append(stat)
        return self


class WithableStatement(Statement):
    """docstring for Withable."""

    def __init__(self, type: StatementType, appHost: Optional[App] = None):
        super().__init__(type)

        # TODO: maybe use weak ref?
        self._appHost = appHost

    def __enter__(self):
        if self._appHost:
            self._appHost._with_temp_host_stack.append(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self._appHost:
            self._appHost._with_temp_host_stack.pop()


class IfStatement(WithableStatement):
    def __init__(
        self, cp: ReactiveComponent, value: Any, appHost: Optional[App] = None
    ):
        super().__init__(StatementType.If, appHost)
        self.targetID = cp.id
        self.value = value
