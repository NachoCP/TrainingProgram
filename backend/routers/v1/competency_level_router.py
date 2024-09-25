from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.services.competency_level_service import CompetencyLevelService
from commons.models.core.competency_level import CompetencyLevel, CompetencyLevelOutput

router = APIRouter(
    prefix="/competency_level",
    tags=["competency_level"]
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=CompetencyLevel)
def create(
    data: CompetencyLevel,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelService(db)
    return _service.create(data)

@router.get("/id/{id}", status_code=status.HTTP_200_OK, response_model=CompetencyLevel)
def get(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelService(db)
    return _service.get(id)

@router.get("", status_code=status.HTTP_200_OK, response_model=List[CompetencyLevel])
def list(
    pageSize: int = 100,
    startIndex: int = 0,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelService(db)
    return _service.list(pageSize, startIndex)


@router.delete("/id/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelService(db)
    return _service.delete(id)

@router.put("/id/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=CompetencyLevel)
def update(
    id: int,
    data: CompetencyLevel,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelService(db)
    return _service.update(id, data)

@router.post("/bulk", status_code=status.HTTP_201_CREATED, response_model=List[CompetencyLevel])
def bulk(
    data: List[CompetencyLevel],
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelService(db)
    return _service.bulk(data)

@router.get("/department/{department_id}", status_code=status.HTTP_200_OK, response_model=List[CompetencyLevelOutput])
def get_all_by_department(
    department_id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = CompetencyLevelService(db)
    return _service.get_all_by_department(department_id)
