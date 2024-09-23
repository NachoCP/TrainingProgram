from typing import List

from sqlalchemy.orm import Session

from backend.models.competency_level import CompetencyLevel
from backend.repositories.sql_alchemy.competency_level_repository import CompetencyLevelRepository
from commons.interfaces.service import IService
from commons.models.core.competency_level import CompetencyLevel as CompetencyLevelSchema
from commons.models.core.competency_level import CompetencyLevelOutput


class CompetencyLevelService(IService[CompetencyLevel, CompetencyLevelSchema]):

    def __init__(self, db: Session) -> None:
        self.repository = CompetencyLevelRepository(db)

    def create(self, schema: CompetencyLevelSchema) -> CompetencyLevel:
        competency = CompetencyLevel(**schema.model_dump(exclude_none=True))
        return self.repository.create(competency)

    def delete(self, id: id) -> None:
        self.repository.delete(id)

    def get(self, id: id) -> CompetencyLevel:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[CompetencyLevel]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: id, schema: CompetencyLevelSchema) -> CompetencyLevel:
        competency = CompetencyLevel(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, competency)

    def bulk(self, schemas: List[CompetencyLevelSchema]) -> List[CompetencyLevel]:
        schema_objects = [CompetencyLevel(**schema.model_dump(exclude_none=True)) for schema in schemas]
        return self.repository.bulk(schema_objects)

    def get_all_by_department(self, department_id: id) -> List[CompetencyLevelOutput]:
        return [CompetencyLevelOutput(**d) for d in self.repository.get_all_by_department(department_id)]
