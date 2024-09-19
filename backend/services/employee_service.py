from typing import List

from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.interfaces.service import IService
from backend.models.employee import Employee
from backend.repositories.sql_alchemy.employee_repository import EmployeeRepository
from backend.schemas.employee import Employee as EmployeeSchema


class EmployeeService(IService[Employee, EmployeeSchema]):

    def __init__(self, db: Session) -> None:
        self.repository = EmployeeRepository(db)

    def create(self, schema: EmployeeSchema) -> Employee:
        employee = Employee(**schema.model_dump(exclude_none=True))
        return self.repository.create(employee)

    def delete(self, id: UUID4) -> None:
        self.repository.delete(id)

    def get(self, id: UUID4) -> Employee:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Employee]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: UUID4, schema: EmployeeSchema) -> Employee:
        employee = Employee(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, employee)
