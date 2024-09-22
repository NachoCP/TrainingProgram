from typing import Optional

from pydantic import BaseModel, Field


class Department(BaseModel):
    id: Optional[int] = Field(description="Unique identifier for the department", example=201)
    name: str = Field(..., description="Name of the department", example="Engineering")

    class Config:
        orm_mode = True
