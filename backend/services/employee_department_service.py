from typing import List

from sqlalchemy.orm import Session

from backend.models.employee_department import EmployeeDepartment
from backend.repositories.sql_alchemy.employee_department_repository import EmployeeDepartmentRepository
from commons.interfaces.service import IService
from commons.models.core.employee_department import EmployeeDepartment as EmployeeDepartmentSchema


class EmployeeDepartmentService(IService[EmployeeDepartment, EmployeeDepartmentSchema]):

    def __init__(self, db: Session) -> None:
        self.repository = EmployeeDepartmentRepository(db)

    def create(self, schema: EmployeeDepartmentSchema) -> EmployeeDepartment:
        department_employee = EmployeeDepartment(**schema.model_dump(exclude_none=True))
        return self.repository.create(department_employee)

    def delete(self, id: id) -> None:
        self.repository.delete(id)

    def get(self, id: id) -> EmployeeDepartment:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[EmployeeDepartment]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: id, schema: EmployeeDepartmentSchema) -> EmployeeDepartment:
        department_employee = EmployeeDepartment(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, department_employee)

    def bulk(self, schemas: List[EmployeeDepartmentSchema]) -> List[EmployeeDepartment]:
        schema_objects = [EmployeeDepartment(**schema.model_dump(exclude_none=True)) for schema in schemas]
        return self.repository.bulk(schema_objects)

