from typing import (
    TypeAlias,
    List,
    Tuple,
    Optional,
    OrderedDict,
    Any,
)

RawSQL: TypeAlias = Tuple[str, Tuple]

CursorDescription: TypeAlias = Optional[Tuple[Tuple]]

ListOrderedDict: TypeAlias = List[OrderedDict[str, Any]]
