from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from commons.enum import RequiredLevelEnum


class EmployeeCompetency(BaseModel):
    id: Optional[int] = Field(description="Unique identifier for the employee competency", example=101)
    employee_id: int = Field(..., description="The ID of the employee", example=1)
    competency_id: int = Field(..., description="The ID of the competency", example=1001)
    current_level: RequiredLevelEnum = Field(
        ..., description="The current level of the competency for the employee", example="Intermediate"
    )
    expiration_date: Optional[date] = Field(
        description="Date when the role or assignment expires", example="2023-12-31", default=None
    )
    effective_date: Optional[date] = Field(
        description="Date when the role became effective", example="2021-06-01", default=None
    )

    model_config = ConfigDict(from_attributes=True)


class EmployeeCompetencyWithoutDates(BaseModel):
    id: Optional[int] = Field(description="Unique identifier for the employee competency", example=101)
    employee_id: int = Field(..., description="The ID of the employee", example=1)
    competency_id: int = Field(..., description="The ID of the competency", example=1001)
    current_level: str = Field(
        ..., description="The current level of the competency for the employee", example="Intermediate"
    )
