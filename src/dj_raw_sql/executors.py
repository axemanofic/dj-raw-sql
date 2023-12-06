from abc import abstractmethod
from typing import TYPE_CHECKING, Protocol

from django.db import connection

from .query_result import EmptyQueryResult, ManyQueryResult, OneQueryResult

if TYPE_CHECKING:
    from .query import Query
    from .query_result import QueryResult


class BaseExecutor(Protocol):
    @abstractmethod
    def fetchall(self, query: "Query") -> "QueryResult":
        raise NotImplementedError

    @abstractmethod
    def fetchone(self, query: "Query") -> "QueryResult":
        raise NotImplementedError

    @abstractmethod
    def execute(self, query: "Query") -> "QueryResult":
        raise NotImplementedError


class Executor(BaseExecutor):
    def fetchall(self, query):
        sql, params = query.sql, query.params
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return ManyQueryResult(
                rows=cursor.fetchall(),
                columns=cursor.description,  # pyright: ignore
                sql=sql,
                params=params,
            )

    def fetchone(self, query):
        sql, params = query.sql, query.params
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return OneQueryResult(
                rows=cursor.fetchone(),
                columns=cursor.description,  # pyright: ignore
                sql=sql,
                params=params,
            )

    def execute(self, query):
        sql, params = query.sql, query.params
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return EmptyQueryResult(
                rows=None,
                columns=None,
                sql=sql,
                params=params,
            )
