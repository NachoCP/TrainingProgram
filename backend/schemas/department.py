from pydantic import BaseModel, Field


class Department(BaseModel):
    id: int = Field(..., description="Unique identifier for the department", example=201)
    name: str = Field(..., description="Name of the department", example="Engineering")
