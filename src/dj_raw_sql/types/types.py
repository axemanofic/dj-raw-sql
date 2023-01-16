from typing import List, Optional, OrderedDict, TypeAlias, Callable

ResultQuery: TypeAlias = Optional[List[OrderedDict]]
DecoratedFunction: TypeAlias = Callable[..., ResultQuery]
