from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Employee(BaseModel):
    id: Optional[int] = Field(description="Unique identifier for the employee", example=1)
    name: str = Field(..., description="Name of the employee", example="John Doe")
    expiration_date: Optional[date] = Field(
        description="Date when the role or assignment expires", example="2023-12-31", default=None
    )
    effective_date: Optional[date] = Field(
        description="Date when the role became effective", example="2021-06-01", default=None
    )

    model_config = ConfigDict(from_attributes=True)


class EmployeeWithoutDates(BaseModel):
    id: Optional[int] = Field(description="Unique identifier for the employee", example=1)
    name: str = Field(..., description="Name of the employee", example="John Doe")

    model_config = ConfigDict(from_attributes=True)
