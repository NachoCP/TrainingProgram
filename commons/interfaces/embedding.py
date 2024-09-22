from abc import ABC, abstractmethod


class IEmbedding( ABC):
    """
    Abstract base embedding to declare the embedder
    """

    @abstractmethod
    def get_embedding(self, text: str) -> None:
        pass
