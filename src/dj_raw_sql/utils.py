from collections import OrderedDict
from typing import Tuple

from dj_raw_sql.types import ResultQuery


def get_sql(get_query, *args, **kwargs) -> Tuple[str, Tuple]:
    sql: str = ""
    params: Tuple = tuple()
    try:
        sql, params = get_query(*args, **kwargs)
    except ValueError:
        sql = get_query()
    return sql, params


def get_list_ordereddict(cursor) -> ResultQuery:
    if cursor.description:
        columns = [column[0] for column in cursor.description]
        return [OrderedDict(zip(columns, row)) for row in cursor.fetchall()]
    return None
