from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Department(BaseModel):
    id: Optional[int] = Field(description="Unique identifier for the department", example=201)
    name: str = Field(..., description="Name of the department", example="Engineering")

    model_config = ConfigDict(from_attributes=True)
