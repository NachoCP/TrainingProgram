from typing import List

from pydantic import UUID4

from backend.interfaces.service import IService
from backend.models.competency_level import CompetencyLevel
from backend.repositories.sql_alchemy.competency_level_repository import CompetencyLevelRepository
from backend.schemas.competency_level import CompetencyLevel as CompetencyLevelSchema


class RulesService(IService[CompetencyLevel, CompetencyLevelSchema]):

    def __init__(self, rulesRepository: CompetencyLevelRepository) -> None:
        self.rulesRepository = rulesRepository

    def create(self, schema: CompetencyLevelSchema) -> CompetencyLevel:
        rule = CompetencyLevel(**schema.model_dump(exclude_none=True))
        return self.rulesRepository.create(rule)

    def delete(self, id: UUID4) -> None:
        self.rulesRepository.delete(id)

    def get(self, id: UUID4) -> CompetencyLevel:
        return self.rulesRepository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[CompetencyLevel]:
        return self.rulesRepository.list(pageSize, startIndex)

    def update(self, id: UUID4, schema: CompetencyLevelSchema) -> CompetencyLevel:
        rule = CompetencyLevel(**schema.model_dump(exclude_none=True))
        return self.rulesRepository.update(id, rule)
