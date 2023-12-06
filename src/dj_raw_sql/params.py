from abc import abstractmethod
from typing import Any, Protocol

class BaseParametres(Protocol):
    @abstractmethod
    def get_params(self) -> tuple:
        raise NotImplementedError


class Parametres(BaseParametres):
    def __init__(self, params: list[Any]) -> None:
        self.params = params

    def get_params(self) -> tuple:
        return tuple(self.params)
