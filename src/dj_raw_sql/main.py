from collections import OrderedDict
from typing import Tuple

from django.db import connection
from django.db.backends.utils import CursorWrapper

from .types import (
    RawSQL,
    Callable,
    ListOrderedDict,
    Columns,
    FetchResult,
)


class BaseQueryExecutor:
    @classmethod
    def get_raw_sql(cls, get_query: Callable, *args, **kwargs) -> RawSQL:
        sql, params = "", ()
        try:
            sql, params = get_query(*args, **kwargs)
        except ValueError:
            sql = get_query()
        return sql, params

    @classmethod
    def fetchall(cls, get_query: Callable, *args, **kwargs):
        pass

    @classmethod
    def fetchone(cls, get_query, *args, **kwargs):
        pass

    @classmethod
    def execute(cls, get_query, *args, **kwargs):
        pass


class QueryExecutor(BaseQueryExecutor):
    @classmethod
    def _get_many_result(cls, cursor: CursorWrapper) -> FetchResult:
        return cursor.fetchall()

    @classmethod
    def _get_result(cls, cursor: CursorWrapper) -> Tuple:
        return cursor.fetchone()

    @classmethod
    def fetchall(cls, get_query: Callable, *args, **kwargs):
        sql, params = cls.get_raw_sql(get_query, *args, **kwargs)
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cls._get_many_result(cursor)

    @classmethod
    def fetchone(cls, get_query, *args, **kwargs):
        sql, params = cls.get_raw_sql(get_query, *args, **kwargs)
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cls._get_result(cursor)

    @classmethod
    def execute(cls, get_query, *args, **kwargs):
        sql, params = cls.get_raw_sql(get_query, *args, **kwargs)
        with connection.cursor() as cursor:
            cursor.execute(sql, params)


class OrderedDictQueryExecutor(QueryExecutor):
    @classmethod
    def __get_columns(cls, cursor: CursorWrapper) -> Columns:
        return [element[0] for element in cursor.description]

    @classmethod
    def _get_many_result(cls, cursor: CursorWrapper) -> ListOrderedDict:
        columns: list[str] = cls.__get_columns(cursor)
        return [OrderedDict(zip(columns, row)) for row in cursor.fetchall()]

    @classmethod
    def _get_result(cls, cursor: CursorWrapper) -> OrderedDict:
        columns: list[str] = cls.__get_columns(cursor)
        row = cursor.fetchone()
        return OrderedDict(zip(columns, row))
