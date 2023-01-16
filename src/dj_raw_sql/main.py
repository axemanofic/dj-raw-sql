from django.db import connection

from dj_raw_sql.types import DecoratedFunction, ResultQuery
from dj_raw_sql.utils import get_list_ordereddict, get_sql


def execute_sql(get_query: DecoratedFunction) -> DecoratedFunction:
    def wrapper(*args, **kwargs) -> ResultQuery:
        sql, params = get_sql(get_query, *args, **kwargs)
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            result = get_list_ordereddict(cursor)
        return result

    return wrapper


def call_procedure(get_query: DecoratedFunction) -> DecoratedFunction:
    def wrapper(*args, **kwargs) -> ResultQuery:
        sql, params = get_sql(get_query, *args, **kwargs)
        with connection.cursor() as cursor:
            cursor.callproc(sql, params)
            result = get_list_ordereddict(cursor)
        return result

    return wrapper
