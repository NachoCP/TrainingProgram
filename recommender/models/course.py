
from typing import List, Literal

from pydantic import Field

from recommender.models.base_dynamic_model import BaseDynamicModel


class CourseModel(BaseDynamicModel):
    title: str = Field(..., description="The course title.")
    matching_competencies: List[str] = Field(
        default_factory=list,
        description="A list of relevant competencies from the provided list (if applicable)."
    )
    course_level: Literal["Beginner", "Intermediate", "Advanced", "Expert"] = Field(
        ..., description="The level of the course, categorized as either Beginner, Intermediate, Advanced, or Expert."
    )

    # Clase interna para la configuración del modelo
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Course Title Example",
                "matching_competencies": [],
                "course_level": "Intermediate"
            }
        }
