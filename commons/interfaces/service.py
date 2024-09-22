from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from pydantic import BaseModel

# Type Definitions
M = TypeVar("M")
S = TypeVar("S", bound=BaseModel)

class IService(ABC, Generic[M, S]):

    @abstractmethod
    def create(self, schema: S) -> M:

        pass

    @abstractmethod
    def delete(self, id: int) -> None:

        pass

    @abstractmethod
    def get(self, id: int) -> M:

        pass

    @abstractmethod
    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[M]:

        pass

    @abstractmethod
    def update(self, id: int, schema: S) -> M:

        pass
