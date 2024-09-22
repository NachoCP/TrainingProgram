from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.services.competency_service import CompetencyService
from commons.models.core.competency import Competency

router = APIRouter(
    prefix="/competency",
    tags=["competency"]
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=Competency)
def create(
    data: Competency,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyService(db)
    return _service.create(data)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Competency)
def get(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyService(db)
    return _service.get(id)

@router.get("", status_code=201, response_model=List[Competency])
def list(
    pageSize: int = 100,
    startIndex: int = 0,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyService(db)
    return _service.list(pageSize, startIndex)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyService(db)
    return _service.delete(id)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=Competency)
def update(
    id: int,
    data: Competency,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyService(db)
    return _service.update(id, data)

@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=List[Competency])
def bulk(
    data: List[Competency],
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyService(db)
    return _service.bulk(data)
