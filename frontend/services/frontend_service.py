from abc import ABC, abstractmethod
from typing import Any, List


class IFrontendService(ABC):
    """
    Abstract base embedding to declare the embedder
    """

    # @abstractmethod
    # def send(self, data: List[Any]) -> None:
    #    pass

    @abstractmethod
    def send_bulk(self, data: List[Any]) -> None:
        pass
