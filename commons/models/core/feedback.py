from pydantic import BaseModel, Field


class Feedback(BaseModel):
    id: int = Field(..., description="Unique identifier for the feedback", example=12345)
    employee_id: int = Field(..., description="Unique identifier for the employee receiving the feedback", example=1001)
    feedback_by: int = Field(..., description="Unique identifier for the person giving the feedback (peer, subordinate, or superior)", example=2001)
    comments: str = Field(..., description="Textual feedback describing the performance of the employee", example="Great teamwork and leadership shown during the project.")
    score: float = Field(None, lt=5.0, description="Optional numeric score associated with the feedback", example=4.5)
    effective_date: str = Field(..., description="Date when the feedback was given", example="2024-09-20")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": 12345,
                    "employee_id": 1001,
                    "feedback_by": 2001,
                    "comments": "Demonstrated excellent communication skills and leadership during the team meetings.",
                    "score": 4.8,
                    "date": "2024-09-20"
                },
                {
                    "id": 12346,
                    "employee_id": 1002,
                    "feedback_by": 2002,
                    "comments": "Needs to improve time management skills to meet project deadlines more consistently.",
                    "score": 3.2,
                    "date": "2024-08-15"
                },
                {
                    "id": 12347,
                    "employee_id": 1003,
                    "feedback_by": 2003,
                    "comments": "Great attention to detail, especially in data analysis tasks.",
                    "score": 4.7,
                    "date": "2024-07-10"
                }
            ]
        }
