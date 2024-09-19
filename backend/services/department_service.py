from typing import List

from sqlalchemy.orm import Session

from backend.interfaces.service import IService
from backend.models.department import Department
from backend.repositories.sql_alchemy.department_repository import DepartmenteRepository
from backend.schemas.department import Department as DepartmentSchema


class DepartmentService(IService[Department, DepartmentSchema]):

    def __init__(self, db: Session) -> None:
        self.repository = DepartmenteRepository(db)

    def create(self, schema: DepartmentSchema) -> Department:
        department = Department(**schema.model_dump(exclude_none=True))
        return self.repository.create(department)

    def delete(self, id: id) -> None:
        self.repository.delete(id)

    def get(self, id: id) -> Department:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Department]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: id, schema: DepartmentSchema) -> Department:
        department = Department(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, department)
