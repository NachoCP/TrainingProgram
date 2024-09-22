from typing import Type

from commons.embeddings.openai import OpenAIEmbeddingProvider
from commons.enum import EmbeddingFactory
from commons.interfaces.embedding import IEmbedding

FACTORY = {
        EmbeddingFactory.openai.value: OpenAIEmbeddingProvider
    }

class EmbeddingProviderFactory:

    @staticmethod
    def get_provider(provider_name: str) -> IEmbedding:
        if provider_name in FACTORY:
            provider_class: Type[IEmbedding] = FACTORY[provider_name]
            return provider_class
        else:
            raise ValueError(f"This embedding provider '{provider_name}' is not supported.")
