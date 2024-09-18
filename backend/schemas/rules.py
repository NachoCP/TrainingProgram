from pydantic import BaseModel, Field

from backend.utils.vocabulary import RequiredLevelEnum


class Rules(BaseModel):
    competency_id: int = Field(..., description="Unique identifier for the competency", example=1001)
    required_level: RequiredLevelEnum = Field(..., description="Required level of competency", example="Advanced")
    num_persona: int = Field(..., description="Number of people required with this competency", example=5)
    company_level: str = Field(..., description="Whether this rule applies at the company or team level", example="Company")
    set_by_id: int = Field(..., description="ID of the manager who set the rule", example=10)
