from typing import Optional

from pydantic import BaseModel, Field


class Competency(BaseModel):
    id: Optional[int] = Field(description="Unique identifier for the competency", example=1001)
    name: str = Field(..., description="Name of the competency", example="Leadership")
    description: str = Field(..., description="Description of the competency", example="Ability to lead teams effectively")

    class Config:
        orm_mode = True
        json_schema_extra={
            "orm_mode": True,
            "examples": [
                {"id": 1, "name": "Leadership", "description": "Ability to lead teams, inspire others, and drive projects to success."},
                {"id": 2, "name": "Creativity", "description": "The ability to generate new ideas and approaches to solve problems effectively."},
                {"id": 3, "name": "Communication", "description": "Skilled in articulating ideas clearly and effectively across teams and clients."},
                {"id": 5, "name": "Data Analysis", "description": "Ability to analyze and interpret complex data for strategic decision-making."},
            ]
        }

