from typing import Protocol
from collections import OrderedDict
from abc import abstractmethod


class BaseQueryResult(Protocol):
    _query_result = None

    @property
    @abstractmethod
    def query_result(self):
        raise NotImplementedError


class QueryResult(BaseQueryResult):
    def __init__(
        self,
        rows: tuple,
        columns: tuple,
        sql: str,
        params: tuple,
    ) -> None:
        self._rows = rows
        self._columns = columns
        self.sql = sql
        self.params = params


class OneQueryResult(QueryResult):
    @property
    def query_result(self):
        if not self._query_result:
            columns = [element[0] for element in self._columns]
            self._query_result = OrderedDict(zip(columns, self._rows))
        return self._query_result


class ManyQueryResult(QueryResult):
    @property
    def query_result(self):
        if not self._query_result:
            columns = [element[0] for element in self._columns]
            self._query_result = [OrderedDict(zip(columns, row)) for row in self._rows]
        return self._query_result
