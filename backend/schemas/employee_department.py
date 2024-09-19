from datetime import date

from pydantic import UUID4, BaseModel, Field

from backend.utils.vocabulary import RoleEnum


class EmployeeDepartment(BaseModel):
    id: UUID4 = Field(..., description="Unique identifier for the department-employee relation", example=301)
    employee_id: UUID4 = Field(..., description="The ID of the employee", example=1)
    department_id: UUID4 = Field(..., description="The ID of the department", example=201)
    role: RoleEnum = Field(..., description="Role of the employee in the department", example="Manager")
    expiration_date: date = Field(None, description="Date when the role or assignment expires", example="2023-12-31")
    effective_date: date = Field(..., description="Date when the role became effective", example="2021-06-01")
