from abc import abstractmethod
from typing import TYPE_CHECKING, Protocol

from django.db import connection

from .query_result import ManyQueryResult

if TYPE_CHECKING:
    from .query import Query


class BaseExecutor(Protocol):
    @abstractmethod
    def fetchall(self, query: "Query"):
        raise NotImplementedError

    @abstractmethod
    def fetchone(self, query: "Query"):
        raise NotImplementedError

    @abstractmethod
    def execute(self, query: "Query"):
        raise NotImplementedError


class Executor(BaseExecutor):
    def fetchall(self, query: "Query") -> "ManyQueryResult":
        sql, params = query.sql, query.params
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return ManyQueryResult(
                rows=cursor.fetchall(),
                columns=cursor.description,
                sql=sql,
                params=params,
            )

    def fetchone(self, query: "Query"):
        sql, params = cls.get_raw_sql(get_query, *args, **kwargs)
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cls._get_result(cursor)

    def execute(self, query: "Query"):
        sql, params = cls.get_raw_sql(get_query, *args, **kwargs)
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
