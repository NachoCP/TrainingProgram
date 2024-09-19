from pydantic import UUID4, BaseModel, Field


class Department(BaseModel):
    id: UUID4 = Field(..., description="Unique identifier for the department", example=201)
    name: str = Field(..., description="Name of the department", example="Engineering")
