from enum import Enum


class EmbeddingFactory(str, Enum):
    openai = "openai"


class LLMFactory(str, Enum):
    openai = "openai"
    anthropic = "anthropic"


class RequiredLevelEnum(str, Enum):
    # Enum for the competency levels
    basic = "basic"  # Entry-level knowledge
    intermediate = "intermediate"  # Mid-level competency
    advanced = "advanced"  # Proficient with advanced understanding
    expert = "expert"  # Mastery in the competency

    @classmethod
    def list_values(cls):
        return [c.value for c in cls]


class RequiredLevelEnumNoBasic(str, Enum):
    # Enum for the competency levels
    intermediate = "intermediate"  # Mid-level competency
    advanced = "advanced"  # Proficient with advanced understanding
    expert = "expert"  # Mastery in the competency


class PriorityType(str, Enum):
    # Enum for the competency levels
    company = "company"  # Mid-level competency
    feedback = "feedback"  # Proficient with advanced understanding
    both = "both"  # Mastery in the competency


level_mapping = {
    RequiredLevelEnum.basic: 0,
    RequiredLevelEnum.intermediate: 1,
    RequiredLevelEnum.advanced: 2,
    RequiredLevelEnum.expert: 3,
}
