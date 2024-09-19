from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: Optional[int] = Field(..., description="Unique identifier for the employee", example=1)
    name: str = Field(..., description="Name of the employee", example="John Doe")
    hire_date: date = Field(..., description="Hire date of the employee", example="2021-05-15")
