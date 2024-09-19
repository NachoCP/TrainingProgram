from typing import List

from backend.interfaces.service import IService
from backend.models.department import Department
from backend.repositories.sql_alchemy.department_repository import DepartmentRepository
from backend.schemas.department import Department as DepartmentSchema


class DepartmentService(IService[Department, DepartmentSchema]):
    def __init__(self, departmentRepository: DepartmentRepository) -> None:
        self.departmentRepository = departmentRepository

    def create(self, schema: DepartmentSchema) -> Department:
        department = Department(**schema.model_dump(exclude_none=True))
        return self.departmentRepository.create(department)

    def delete(self, id: int) -> None:
        self.departmentRepository.delete(id)

    def get(self, id: int) -> Department:
        return self.departmentRepository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Department]:
        return self.departmentRepository.list(pageSize, startIndex)

    def update(self, id: int, schema: DepartmentSchema) -> Department:
        department = Department(**schema.model_dump(exclude_none=True))
        return self.departmentRepository.update(id, department)
