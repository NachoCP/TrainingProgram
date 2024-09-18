from pydantic import BaseModel, Field

from backend.utils.vocabulary import TypeEnum


class Competency(BaseModel):
    competency_id: int = Field(..., description="Unique identifier for the competency", example=1001)
    name: str = Field(..., description="Name of the competency", example="Leadership")
    type: TypeEnum = Field(..., description="Competency type, either Global or Team-specific", example="Global")
    description: str = Field(..., description="Description of the competency", example="Ability to lead teams effectively")
