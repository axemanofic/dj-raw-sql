from typing import TYPE_CHECKING, Protocol
from abc import abstractmethod

if TYPE_CHECKING:
    from .params import BaseParametres


class BaseQuery(Protocol):
    @property
    @abstractmethod
    def sql(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def params(self) -> tuple:
        raise NotImplementedError


class Query(BaseQuery):
    def __init__(self, raw_sql, params: "BaseParametres | None" = None) -> None:
        self._raw_sql = raw_sql
        self._params = params

    @property
    def sql(self) -> str:
        """The sql property."""
        return self._raw_sql

    @property
    def params(self) -> tuple:
        if self._params:
            return tuple(self._params.get_params())
        return tuple([self._params])
