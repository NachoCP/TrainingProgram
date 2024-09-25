from abc import ABC, abstractmethod
from typing import Any


class IRanking(ABC):
    """
    Abstract base class for a recommendation system with steps for candidate generation,
    filtering, scoring, and ordering.
    """

    @abstractmethod
    def filtering(self, candidates: Any) -> Any:
        """
        Filter the candidate items.
        :param candidates: The list or set of candidate items.
        :return: A filtered list or set of items.
        """
        pass

    @abstractmethod
    def scoring(self, filtered_data: Any) -> Any:
        """
        Score the filtered items based on relevance.
        :param filtered_data: The list or set of filtered items.
        :return: Scored items, typically a list with scores.
        """
        pass

    @abstractmethod
    def ordering(self, scored_data: Any) -> Any:
        """
        Order the scored items by their relevance or priority.
        :param scored_data: The list or set of scored items.
        :return: A ranked list or set of items based on their scores.
        """
        pass
