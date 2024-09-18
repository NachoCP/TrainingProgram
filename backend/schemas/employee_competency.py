from datetime import date

from pydantic import BaseModel, Field


class EmployeeCompetency(BaseModel):
    id: int = Field(..., description="Unique identifier for the employee competency", example=101)
    employee_id: int = Field(..., description="The ID of the employee", example=1)
    competency_id: int = Field(..., description="The ID of the competency", example=1001)
    current_level: str = Field(..., description="The current level of the competency for the employee", example="Intermediate")
    assigned_date: date = Field(..., description="The date the competency was assigned to the employee", example="2022-03-10")
