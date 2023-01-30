from collections import OrderedDict
from typing import Tuple, Callable, Optional

from dj_raw_sql.types import (
    RawSQL,
    CursorDescription,
    ListOrderedDict,
)


def get_raw_sql(get_query: Callable, *args, **kwargs) -> RawSQL:
    sql, params = "", ()
    try:
        sql, params = get_query(*args, **kwargs)
    except ValueError:
        sql = get_query()
    return sql, params


def get_list_ordereddict(
    description: CursorDescription,
    data: Tuple,
) -> Optional[ListOrderedDict]:
    if description:
        columns: list[str] = [element[0] for element in description]
        return [OrderedDict(zip(columns, row)) for row in data]
    return None
