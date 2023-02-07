from dj_raw_sql.utils import get_list_ordereddict, get_raw_sql
from django.db import connection


def execute_sql(to_ordereddict=False):
    def wrapper(get_query):
        def main(*args, **kwargs):
            sql, params = get_raw_sql(get_query, *args, **kwargs)
            with connection.cursor() as cursor:
                cursor.execute(sql, params)
                if to_ordereddict:
                    return get_list_ordereddict(cursor)
                return cursor.fetchall()

        return main

    return wrapper


def call_procedure(
    procedure_name: str,
    params=None,
    kparams=None,
):
    with connection.cursor() as cursor:
        cursor.callproc(
            procname=procedure_name,
            params=params,
            kparams=kparams,
        )
        return cursor.fetchall()
