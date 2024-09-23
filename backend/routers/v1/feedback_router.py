from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.services.feedback_service import FeedbackService
from commons.models.core.feedback import Feedback

router = APIRouter(
    prefix="/feedback",
    tags=["feedback"]
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=Feedback)
def create(
    data: Feedback,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = FeedbackService(db)
    return _service.create(data)

@router.get("/id/{id}", status_code=status.HTTP_200_OK, response_model=Feedback)
def get(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = FeedbackService(db)
    return _service.get(id)

@router.get("", status_code=201, response_model=List[Feedback])
def list(
    pageSize: int = 100,
    startIndex: int = 0,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = FeedbackService(db)
    return _service.list(pageSize, startIndex)


@router.delete("/id/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = FeedbackService(db)
    return _service.delete(id)

@router.put("/id/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=Feedback)
def update(
    id: int,
    data: Feedback,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = FeedbackService(db)
    return _service.update(id, data)

@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=List[Feedback])
def bulk(
    data: List[Feedback],
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = FeedbackService(db)
    return _service.bulk(data)

@router.get("/employee_id/{id}", status_code=status.HTTP_200_OK, response_model=List[Feedback])
def get_all_by_employee(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = FeedbackService(db)
    return _service.get_all_by_employee(id)
