from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.services.employee_service import EmployeeService
from commons.models.core.employee import Employee, EmployeeWithoutDates

router = APIRouter(prefix="/employee", tags=["employee"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=Employee)
def create(data: Employee, db: Session = Depends(get_db_connection)):  # noqa: B008
    _service = EmployeeService(db)
    return _service.create(data)


@router.get("/id/{id}", status_code=status.HTTP_200_OK, response_model=Employee)
def get(id: int, db: Session = Depends(get_db_connection)):  # noqa: B008
    _service = EmployeeService(db)
    return _service.get(id)


@router.get("", status_code=status.HTTP_200_OK, response_model=List[Employee])
def list(pageSize: int = 100, startIndex: int = 0, db: Session = Depends(get_db_connection)):  # noqa: B008
    _service = EmployeeService(db)
    return _service.list(pageSize, startIndex)


@router.delete("/id/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db_connection)):  # noqa: B008
    _service = EmployeeService(db)
    return _service.delete(id)


@router.put("/id/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=Employee)
def update(id: int, data: Employee, db: Session = Depends(get_db_connection)):  # noqa: B008
    _service = EmployeeService(db)
    return _service.update(id, data)


@router.post("/bulk", status_code=status.HTTP_201_CREATED, response_model=List[Employee])
def bulk(data: List[EmployeeWithoutDates], db: Session = Depends(get_db_connection)):  # noqa: B008
    _service = EmployeeService(db)
    return _service.bulk(data)


@router.get(
    "/department/{department_id}", status_code=status.HTTP_202_ACCEPTED, response_model=List[EmployeeWithoutDates]
)
def get_all_by_department(department_id: int, db: Session = Depends(get_db_connection)):  # noqa: B008
    _service = EmployeeService(db)
    return _service.get_all_by_department(department_id)
