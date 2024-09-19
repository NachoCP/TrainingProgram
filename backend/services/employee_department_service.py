from typing import List

from backend.interfaces.service import IService
from backend.models.employee_department import EmployeeDepartment
from backend.repositories.sql_alchemy.employee_department_repository import EmployeeDepartmentRepository
from backend.schemas.employee_department import EmployeeDepartment as EmployeeDepartmentSchema


class DepartmentEmployeeService(IService[EmployeeDepartment, EmployeeDepartmentSchema]):
    def __init__(self, departmentEmployeeRepository: EmployeeDepartmentRepository) -> None:
        self.departmentEmployeeRepository = departmentEmployeeRepository

    def create(self, schema: EmployeeDepartmentSchema) -> EmployeeDepartment:
        department_employee = EmployeeDepartment(**schema.model_dump(exclude_none=True))
        return self.departmentEmployeeRepository.create(department_employee)

    def delete(self, id: int) -> None:
        self.departmentEmployeeRepository.delete(id)

    def get(self, id: int) -> EmployeeDepartment:
        return self.departmentEmployeeRepository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[EmployeeDepartment]:
        return self.departmentEmployeeRepository.list(pageSize, startIndex)

    def update(self, id: int, schema: EmployeeDepartmentSchema) -> EmployeeDepartment:
        department_employee = EmployeeDepartment(**schema.model_dump(exclude_none=True))
        return self.departmentEmployeeRepository.update(id, department_employee)
