from pydantic import UUID4, BaseModel, Field


class Competency(BaseModel):
    competency_id: UUID4 = Field(..., description="Unique identifier for the competency", example=1001)
    name: str = Field(..., description="Name of the competency", example="Leadership")
    description: str = Field(..., description="Description of the competency", example="Ability to lead teams effectively")
