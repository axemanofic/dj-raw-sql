from typing import TYPE_CHECKING, NamedTuple, Protocol
from collections import OrderedDict
from abc import abstractmethod

if TYPE_CHECKING:
    from typing import List, Tuple, Any, Optional


class Column(NamedTuple):
    name: "Optional[str]"
    type_code: "Optional[int]"
    display_size: "Optional[int]"
    internal_size: "Optional[int]"
    precision: "Optional[int]"
    scale: "Optional[int]"
    null_ok: None
    table_column: "Optional[str]"
    table_oid: "Optional[int]"


class BaseQueryResult(Protocol):
    @property
    @abstractmethod
    def query_result(self):
        raise NotImplementedError

    @abstractmethod
    def _get_columns_name(self):
        raise NotImplementedError


class QueryResult(BaseQueryResult):
    def __init__(
        self,
        rows: "Any",
        columns: "Optional[Tuple[Column, ...]]",
        sql: str,
        params: "Tuple",
    ) -> None:
        self._rows = rows
        self._columns = columns
        self.sql = sql
        self.params = params

    @property
    def query_result(self):
        raise NotImplementedError

    def _get_columns_name(self) -> "List[str | None]":
        if self._columns:
            return [column[0] for column in self._columns]
        else:
            return []


class OneQueryResult(QueryResult):
    _rows: "Tuple[Any, ...] | None"

    def __init__(
        self,
        rows: "Tuple[Any, ...] | None",
        columns: "Optional[Tuple[Column, ...]]",
        sql: str,
        params: "Tuple",
    ) -> None:
        super().__init__(rows, columns, sql, params)

    @property
    def query_result(self):
        columns_name = self._get_columns_name()
        if self._rows:
            return OrderedDict(zip(columns_name, self._rows))
        else:
            return None


class ManyQueryResult(QueryResult):
    _rows: "List[Tuple[Any, ...]]"

    def __init__(
        self,
        rows: "List[Tuple[Any, ...]]",
        columns: "Optional[Tuple[Column, ...]]",
        sql: str,
        params: "Tuple",
    ) -> None:
        super().__init__(rows, columns, sql, params)

    @property
    def query_result(self):
        columns_name = self._get_columns_name()
        return [OrderedDict(zip(columns_name, row)) for row in self._rows]


class EmptyQueryResult(QueryResult):
    def __init__(
        self,
        rows: "None",
        columns: "None",
        sql: str,
        params: "Tuple",
    ) -> None:
        super().__init__(rows, columns, sql, params)

    @property
    def query_result(self):
        return None
