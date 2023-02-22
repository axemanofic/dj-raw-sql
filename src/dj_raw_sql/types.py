from typing import Any, List, OrderedDict, Tuple, TypeAlias, Callable

RawSQL: TypeAlias = Tuple[str, Tuple]

ListOrderedDict: TypeAlias = List[OrderedDict[str, Any]]

Columns: TypeAlias = List[str]

FetchResult: TypeAlias = Tuple[Tuple]
