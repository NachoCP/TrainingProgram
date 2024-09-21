from typing import Type

from recommender.enum import LLMFactory
from recommender.interfaces.llm import ILLM
from recommender.llm.openai import OpenAIRunner

FACTORY = {
        LLMFactory.openai.value: OpenAIRunner
    }

class LLMProviderFactory:

    @staticmethod
    def get_provider(provider_name: str) -> ILLM:
        if provider_name in FACTORY:
            provider_class: Type[ILLM] = FACTORY[provider_name]
            return provider_class
        else:
            raise ValueError(f"This llm provider '{provider_name}' is not supported.")
