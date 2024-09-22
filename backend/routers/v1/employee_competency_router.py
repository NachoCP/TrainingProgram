from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.services.employee_competency_service import EmployeeCompetencyService
from commons.models.core.employee_competency import EmployeeCompetency

router = APIRouter(
    prefix="/employee-competencies",
    tags=["employee-competency"]
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=EmployeeCompetency)
def create(
    data: EmployeeCompetency,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.create(data)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=EmployeeCompetency)
def get(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.get(id)

@router.get("", status_code=201, response_model=List[EmployeeCompetency])
def list(
    pageSize: int = 100,
    startIndex: int = 0,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.list(pageSize, startIndex)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.delete(id)

@router.put("/{id}", status_code=201, response_model=EmployeeCompetency)
def update(
    id: int,
    data: EmployeeCompetency,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.update(id, data)

@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=List[EmployeeCompetency])
def bulk(
    data: List[EmployeeCompetency],
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.bulk(data)
