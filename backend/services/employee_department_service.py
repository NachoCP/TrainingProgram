from typing import List

from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.interfaces.service import IService
from backend.models.employee_department import EmployeeDepartment
from backend.repositories.sql_alchemy.employee_department_repository import EmployeeDepartmentRepository
from backend.schemas.employee_department import EmployeeDepartment as EmployeeDepartmentSchema


class DepartmentEmployeeService(IService[EmployeeDepartment, EmployeeDepartmentSchema]):

    def __init__(self, db: Session) -> None:
        self.repository = EmployeeDepartmentRepository(db)

    def create(self, schema: EmployeeDepartmentSchema) -> EmployeeDepartment:
        department_employee = EmployeeDepartment(**schema.model_dump(exclude_none=True))
        return self.repository.create(department_employee)

    def delete(self, id: UUID4) -> None:
        self.repository.delete(id)

    def get(self, id: UUID4) -> EmployeeDepartment:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[EmployeeDepartment]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: UUID4, schema: EmployeeDepartmentSchema) -> EmployeeDepartment:
        department_employee = EmployeeDepartment(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, department_employee)
