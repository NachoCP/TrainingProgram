from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.services.employee_competency_service import EmployeeCompetencyService
from commons.models.core.competency_level import (
    CompetencyLevelDepartmentOutput,
    CompetencyLevelEmployeeOutput,
    CompetencyLevelOutput,
)
from commons.models.core.employee_competency import EmployeeCompetency, EmployeeCompetencyWithoutDates

router = APIRouter(
    prefix="/employee_competency",
    tags=["employee_competency"]
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=EmployeeCompetency)
def create(
    data: EmployeeCompetency,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.create(data)

@router.get("/id/{id}", status_code=status.HTTP_200_OK, response_model=EmployeeCompetency)
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


@router.delete("/id/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.delete(id)

@router.put("/id/{id}", status_code=201, response_model=EmployeeCompetency)
def update(
    id: int,
    data: EmployeeCompetency,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.update(id, data)

@router.post("/bulk", status_code=status.HTTP_200_OK, response_model=List[EmployeeCompetencyWithoutDates])
def bulk(
    data: List[EmployeeCompetencyWithoutDates],
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.bulk(data)

@router.get("/employee/{id}", status_code=status.HTTP_200_OK, response_model=List[CompetencyLevelEmployeeOutput])
def get_all_by_employee(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.get_all_by_employee(id)

@router.get("/group/department/{department_id}", status_code=status.HTTP_200_OK, response_model=List[CompetencyLevelOutput])
def group_competency_level_by_employee_ids(
    department_id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.group_competency_level_by_employee_ids(department_id)

@router.get("/department/{department_id}", status_code=status.HTTP_200_OK, response_model=List[CompetencyLevelDepartmentOutput])
def get_all_by_department(
    department_id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = EmployeeCompetencyService(db)
    return _service.get_all_by_department(department_id)
