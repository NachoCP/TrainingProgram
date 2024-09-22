from enum import Enum


class EmbeddingFactory(str, Enum):
    openai = "openai"

class LLMFactory(str, Enum):
    openai = "openai"
