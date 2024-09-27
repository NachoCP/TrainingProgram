from typing import List

from sqlalchemy.orm import Session

from backend.models.employee import Employee
from backend.repositories.sql_alchemy.employee_department_repository import EmployeeDepartmentRepository
from backend.repositories.sql_alchemy.employee_repository import EmployeeRepository
from commons.interfaces.service import IService
from commons.models.core.employee import Employee as EmployeeSchema
from commons.models.core.employee import EmployeeWithoutDates


class EmployeeService(IService[Employee, EmployeeSchema]):

    def __init__(self, db: Session) -> None:
        self.repository = EmployeeRepository(db)
        self.employee_department_repository = EmployeeDepartmentRepository(db)

    def create(self, schema: EmployeeSchema) -> Employee:
        employee = Employee(**schema.model_dump(exclude_none=True))
        return self.repository.create(employee)

    def delete(self, id: id) -> None:
        self.repository.delete(id)

    def get(self, id: id) -> Employee:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Employee]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: id, schema: EmployeeSchema) -> Employee:
        employee = Employee(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, employee)

    def bulk(self, schemas: List[EmployeeSchema]) -> List[Employee]:
        schema_objects = [Employee(**schema.model_dump(exclude_none=True)) for schema in schemas]
        return self.repository.bulk(schema_objects)

    def get_all_by_department(self, department_id: int) -> List[EmployeeWithoutDates]:
        return [
            EmployeeWithoutDates(**d) for d in self.employee_department_repository.get_all_by_department(department_id)
        ]
