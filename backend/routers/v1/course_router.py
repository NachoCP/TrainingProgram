from typing import List

from fastapi import APIRouter, Depends, status
from pymilvus import MilvusClient
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection, get_milvus_connection
from backend.services.course_service import CourseService
from commons.models.core.course import Course
from commons.models.recommender.course import CourseMatching

router = APIRouter(
    prefix="/course",
    tags=["course"]
)


@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=List[Course])
def bulk(
    db: Session = Depends(get_db_connection),  # noqa: B008
    client: MilvusClient = Depends(get_milvus_connection)  # noqa: B008
):
    _service = CourseService(db, client)
    return _service.bulk()

@router.get("/recommend_course/{id}", status_code=201, response_model=CourseMatching)
def recommend_courses(
    id: int,
    db: Session = Depends(get_db_connection), # noqa: B008
    client: MilvusClient = Depends(get_milvus_connection)  # noqa: B008
):
    _service = CourseService(db, client)
    return _service.recommend_courses(id)
