from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

M = TypeVar("M")  # Model Type
K = TypeVar("K")  # Key Type (e.g., ID)


class IRepository(Generic[M, K], ABC):
    """
    Abstract base repository defining CRUD methods for all entities.
    """

    @abstractmethod
    def create(self, instance: M) -> M:
        pass

    @abstractmethod
    def get(self, id: K) -> M:
        pass

    @abstractmethod
    def list(self, limit: int, start: int) -> List[M]:
        pass

    @abstractmethod
    def update(self, id: K, instance: M) -> M:
        pass

    @abstractmethod
    def delete(self, id: K) -> None:
        pass
