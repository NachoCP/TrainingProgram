from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.services.competency_level_service import CompetencyLevelRepository
from commons.models.core.competency_level import CompetencyLevel

router = APIRouter(
    prefix="/competency_level",
    tags=["competency_level"]
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=CompetencyLevel)
def create(
    data: CompetencyLevel,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelRepository(db)
    return _service.create(data)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CompetencyLevel)
def get(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelRepository(db)
    return _service.get(id)

@router.get("", status_code=201, response_model=List[CompetencyLevel])
def list(
    pageSize: int = 100,
    startIndex: int = 0,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelRepository(db)
    return _service.list(pageSize, startIndex)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelRepository(db)
    return _service.delete(id)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=CompetencyLevel)
def update(
    id: int,
    data: CompetencyLevel,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelRepository(db)
    return _service.update(id, data)

@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=List[CompetencyLevel])
def bulk(
    data: List[CompetencyLevel],
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelRepository(db)
    return _service.bulk(data)
