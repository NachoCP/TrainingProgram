from enum import Enum


class EmbeddingFactory(str, Enum):
    openai = "openai"

class LLMFactory(str, Enum):
    openai = "openai"

class RequiredLevelEnum(str, Enum):
    # Enum for the competency levels
    basic = "basic"  # Entry-level knowledge
    intermediate = "intermediate"  # Mid-level competency
    advanced = "advanced"  # Proficient with advanced understanding
    expert = "expert"  # Mastery in the competency

required_level_weights = {
    RequiredLevelEnum.basic: 1,
    RequiredLevelEnum.intermediate: 2,
    RequiredLevelEnum.advanced: 3,
    RequiredLevelEnum.expert: 4
}
