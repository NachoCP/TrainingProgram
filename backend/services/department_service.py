from typing import List

from sqlalchemy.orm import Session

from backend.models.department import Department
from backend.repositories.sql_alchemy.department_repository import DepartmenteRepository
from commons.interfaces.service import IService
from commons.logging import logger
from commons.models.core.department import Department as DepartmentSchema


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

    def bulk(self, schemas: List[DepartmentSchema]) -> List[Department]:
        logger.info(f"Dumping the following number of departments {len(schemas)}")
        schema_objects = [Department(**schema.model_dump(exclude_none=True)) for schema in schemas]
        return self.repository.bulk(schema_objects)
