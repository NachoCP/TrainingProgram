from typing import List

from backend.interfaces.service import IService
from backend.models.employee import Employee
from backend.repositories.sql_alchemy.employee_repository import EmployeeRepository
from backend.schemas.employee import Employee as EmployeeSchema


class EmployeeService(IService[Employee, EmployeeSchema]):
    def __init__(self, employeeRepository: EmployeeRepository) -> None:
        self.employeeRepository = employeeRepository

    def create(self, schema: EmployeeSchema) -> Employee:
        employee = Employee(schema.model_dump())
        return self.employeeRepository.create(employee)

    def delete(self, id: int) -> None:
        self.employeeRepository.delete(id)

    def get(self, id: int) -> Employee:
        return self.employeeRepository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Employee]:
        return self.employeeRepository.list(pageSize, startIndex)

    def update(self, id: int, schema: EmployeeSchema) -> Employee:
        employee = Employee(schema.model_dump())
        return self.employeeRepository.update(id, employee)
