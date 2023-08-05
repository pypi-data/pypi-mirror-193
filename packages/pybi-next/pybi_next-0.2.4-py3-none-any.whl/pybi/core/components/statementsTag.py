from enum import Enum


class StatementType(Enum):
    Init = "Init"
    Component = "Component"
    DataSource = "DataSource"
    For = "For"
    If = "If"
