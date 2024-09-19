from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.schemas.department import Department
from backend.services.department_service import DepartmentService

router = APIRouter(
    prefix="/department",
    tags=["department"]
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=Department)
def create(
    data: Department,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = DepartmentService(db)
    return _service.create(data)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Department)
def get(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = DepartmentService(db)
    return _service.get(id)

@router.get("", status_code=201, response_model=List[Department])
def list(
    pageSize: int = 100,
    startIndex: int = 0,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = DepartmentService(db)
    return _service.list(pageSize, startIndex)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = DepartmentService(db)
    return _service.delete(id)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=Department)
def update(
    id: int,
    data: Department,
    db: Session = Depends(get_db_connection)  # noqa: B008
):
    _service = DepartmentService(db)
    return _service.update(id, data)
