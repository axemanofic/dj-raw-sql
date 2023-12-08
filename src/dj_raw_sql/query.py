from typing import TYPE_CHECKING, Protocol
from abc import abstractmethod

if TYPE_CHECKING:
    from typing import List, Any, Tuple


class BaseQuery(Protocol):
    @property
    @abstractmethod
    def sql(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def params(self) -> "Tuple[Any, ...]":
        raise NotImplementedError


class Query(BaseQuery):
    def __init__(self, raw_sql: str, params: "List[Any] | None" = None) -> None:
        self._raw_sql = raw_sql
        self._params = params

    @property
    def sql(self):
        """The sql property."""
        return self._raw_sql

    @property
    def params(self):
        if self._params:
            return tuple(self._params)
        else:
            return tuple()
