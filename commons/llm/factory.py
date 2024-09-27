from typing import Type

from commons.enum import LLMFactory
from commons.interfaces.llm import ILLM
from commons.llm.anthropic import AnthropicRunner
from commons.llm.openai import OpenAIRunner
from commons.logging import logger

FACTORY = {LLMFactory.openai.value: OpenAIRunner, LLMFactory.anthropic.value: AnthropicRunner}


class LLMProviderFactory:

    @staticmethod
    def get_provider(provider_name: str) -> ILLM:
        if provider_name in FACTORY:
            logger.info(f"Selected the following provider {provider_name}")
            provider_class: Type[ILLM] = FACTORY[provider_name]
            return provider_class
        else:
            logger.error(f"This llm provider '{provider_name}' is not supported.")
            raise ValueError(f"This llm provider '{provider_name}' is not supported.")

