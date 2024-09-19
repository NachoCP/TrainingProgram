from pydantic import UUID4, BaseModel, Field

from backend.utils.vocabulary import RequiredLevelEnum


class CompetencyLevel(BaseModel):
    id: UUID4 = Field(..., description="Unique identifier for the competency level")
    competency_id: UUID4 = Field(..., description="Unique identifier for the competency", example=1001)
    required_level: RequiredLevelEnum = Field(..., description="Required level of competency", example="Advanced")
    num_persona: int = Field(..., description="Number of people required with this competency", example=5)
