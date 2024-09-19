from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from pydantic import BaseModel

# Type Definitions
M = TypeVar("M")  # Model Type
S = TypeVar("S", bound=BaseModel)  # Pydantic Schema Type
K = TypeVar("K")  # Key Type (e.g., ID)

class IService(ABC, Generic[M, S]):

    @abstractmethod
    def create(self, schema: S) -> M:

        pass

    @abstractmethod
    def delete(self, id: K) -> None:

        pass

    @abstractmethod
    def get(self, id: K) -> M:

        pass

    @abstractmethod
    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[M]:

        pass

    @abstractmethod
    def update(self, id: K, schema: S) -> M:

        pass
