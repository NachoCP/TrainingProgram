from typing import List

from backend.models.competency_level import CompetencyLevel
from backend.repositories.sql_alchemy.competency_level_repository import CompetencyLevelRepository
from commons.interfaces.service import IService
from commons.models.core.competency_level import CompetencyLevel as CompetencyLevelSchema


class RulesService(IService[CompetencyLevel, CompetencyLevelSchema]):

    def __init__(self, rulesRepository: CompetencyLevelRepository) -> None:
        self.rulesRepository = rulesRepository

    def create(self, schema: CompetencyLevelSchema) -> CompetencyLevel:
        rule = CompetencyLevel(**schema.model_dump(exclude_none=True))
        return self.rulesRepository.create(rule)

    def delete(self, id: id) -> None:
        self.rulesRepository.delete(id)

    def get(self, id: id) -> CompetencyLevel:
        return self.rulesRepository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[CompetencyLevel]:
        return self.rulesRepository.list(pageSize, startIndex)

    def update(self, id: id, schema: CompetencyLevelSchema) -> CompetencyLevel:
        rule = CompetencyLevel(**schema.model_dump(exclude_none=True))
        return self.rulesRepository.update(id, rule)

    def bulk(self, schemas: List[CompetencyLevelSchema]) -> List[CompetencyLevel]:
        schema_objects = [CompetencyLevel(**schema.model_dump(exclude_none=True)) for schema in schemas]
        return self.repository.bulk(schema_objects)

