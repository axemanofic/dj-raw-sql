from collections import OrderedDict
from typing import Callable, Optional

from dj_raw_sql.types import ListOrderedDict, RawSQL


def get_raw_sql(get_query: Callable, *args, **kwargs) -> RawSQL:
    sql, params = "", ()
    try:
        sql, params = get_query(*args, **kwargs)
    except ValueError:
        sql = get_query()
    return sql, params


def get_list_ordereddict(cursor) -> Optional[ListOrderedDict]:
    if cursor.description:
        columns: list[str] = [element[0] for element in cursor.description]
        return [OrderedDict(zip(columns, row)) for row in cursor.fetchall()]
    return None
