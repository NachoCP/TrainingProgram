from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.models.employee_department import EmployeeDepartment
from backend.repositories.sql_alchemy.base_repository import BaseRepository


class EmployeeDepartmentRepository(BaseRepository[EmployeeDepartment, UUID4]):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
