from abc import ABC, abstractmethod
from typing import Any


class ILLM( ABC):
    """
    Abstract base llm to declare the llm
    """

    @abstractmethod
    def run(self, **kwargs: Any) -> Any:
        pass
