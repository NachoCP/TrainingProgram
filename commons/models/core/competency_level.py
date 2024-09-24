from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from commons.enum import RequiredLevelEnum


class CompetencyLevel(BaseModel):
    id: Optional[int] = Field(description="Unique identifier for the competency level")
    competency_id: int = Field(..., description="Unique identifier for the competency", example=1001)
    department_id: int = Field(..., description="Unique identifier for the department", example=1001)
    required_level: RequiredLevelEnum = Field(..., description="Required level of competency", example="Advanced")
    num_workers: int = Field(..., description="Number of people required with this competency", example=5)

    model_config = ConfigDict(from_attributes=True)

class CompetencyLevelOutput(BaseModel):
    name: str = Field(..., description="Name of the competency", example="Leadership")
    required_level: RequiredLevelEnum = Field(..., description="Required level of competency", example="Advanced")
    num_workers: int = Field(..., description="Number of people required with this competency", example=5)

    model_config = ConfigDict(from_attributes=True)

class CompetencyLevelEmployeeOutput(BaseModel):
    competency_name: str = Field(..., description="Name of the competency", example="Leadership")
    employee_name: str = Field(..., description="Name of the employee assigned to this competency")
    employee_id: int = Field(..., description="Employee Id")
    required_level: RequiredLevelEnum = Field(..., description="Required level of competency", example="Advanced")

    model_config = ConfigDict(from_attributes=True)

class CompetencyLevelGrouped(BaseModel):
    name: str = Field(..., description="Name of the competency", example="Leadership")
    required_level: RequiredLevelEnum = Field(..., description="Required level of competency", example="Advanced")
    num_workers: int = Field(..., description="Number of people required with this competency", example=5)

    model_config = ConfigDict(from_attributes=True)
