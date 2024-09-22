
from typing import List, Literal, Optional

from pydantic import Field

from commons.models.base_dynamic_model import BaseDynamicModel


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


class CourseModelOutput(BaseDynamicModel):
    metric_coefficient: Optional[float]
    query_embedding: List[float]
    query_string: Optional[str]
    category: Optional[str]
    course_type: Optional[str]
    instructors: Optional[str]
    language: Optional[str]
    level: Optional[str]
    matching_competencies: Optional[str]
    number_of_reviews: Optional[int]
    number_of_viewers: Optional[int]
    prequisites: Optional[str]
    rating: Optional[float]
    short_intro: Optional[str]
    site: Optional[str]
    skills: Optional[str]
    sub_category: Optional[str]
    subtitle_languages: Optional[str]
    title: Optional[str]
    url: Optional[str]
    final_score: Optional[float] = Field(default=0.0)
