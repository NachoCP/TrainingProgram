from typing import List, Optional

from pydantic import BaseModel, Field


class Course(BaseModel):
    # Metadata fields
    title: str = Field(..., description="Title of the course")
    url: str = Field(..., description="URL of the course")
    short_intro: Optional[str] = Field(None, description="Short introduction of the course")
    category: str = Field(..., description="Category of the course")
    sub_category: Optional[str] = Field(None, description="Sub-category of the course")
    course_type: Optional[str] = Field(None, description="Type of the course (e.g., video, text)")
    language: str = Field(..., description="Language of the course")
    subtitle_languages: Optional[str] = Field(None, description="Languages available for subtitles")
    skills: Optional[str] = Field(None,  description="Skills covered in the course")
    instructors: Optional[str] = Field(None, description="Instructors of the course")

    rating: Optional[float] = Field(None, description="Rating of the course")
    number_of_viewers: Optional[float] = Field(None, description="Number of viewers of the course")

    site: Optional[str] = Field(None, description="The platform/site hosting the course")
    level: Optional[str] = Field(None,  description="Level of the course (beginner, intermediate, advanced)")
    number_of_reviews: Optional[int] = Field(None, description="Number of reviews for the course")
    prequisites: Optional[str] = Field(None, description="Pre-requisites for the course")
    matching_competencies: Optional[str] = Field(None,  description="Competencies matched by the course")
    course_level: Optional[str] = Field(None, description="Course level (e.g., beginner, expert)")

    embedding: List[float] = Field(..., description="Embedding vector for the course")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Introduction to Machine Learning",
                "url": "https://example.com/course/intro-to-ml",
                "short_intro": "Learn the fundamentals of Machine Learning in this introductory course.",
                "category": "Data Science",
                "sub_category": "Machine Learning",
                "course_type": "Video",
                "language": "English",
                "subtitle_languages": "English, Spanish",
                "skills": "Machine Learning, Python, Statistics",
                "instructors": "John Doe, Jane Smith",
                "rating": 4.8,
                "number_of_viewers": 50000.0,
                "site": "Coursera",
                "level": "Beginner",
                "number_of_reviews": 1200,
                "prequisites": "Basic Python knowledge",
                "matching_competencies": "Data Analysis, AI Development",
                "course_level": "Beginner",
                "embedding": [0.1, 0.5, -0.2, 0.8, 0.6]
            }
        }
