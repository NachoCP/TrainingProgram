from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class EmployeeDepartment(BaseModel):
    id: Optional[int] = Field(description="Unique identifier for the department-employee relation", example=301)
    employee_id: int = Field(..., description="The ID of the employee", example=1)
    department_id: int = Field(..., description="The ID of the department", example=201)
    expiration_date: Optional[date] = Field(description="Date when the role or assignment expires", example="2023-12-31", default=None)
    effective_date: date = Field(description="Date when the role became effective", example="2021-06-01", default=None)

    model_config = ConfigDict(from_attributes=True)
