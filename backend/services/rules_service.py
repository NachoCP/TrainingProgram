from typing import List

from backend.interfaces.service import IService
from backend.models.competency_level import Rules
from backend.repositories.sql_alchemy.competency_level_repository import RulesRepository
from backend.schemas.competency_level import Rules as RulesSchema


class RulesService(IService[Rules, RulesSchema]):
    def __init__(self, rulesRepository: RulesRepository) -> None:
        self.rulesRepository = rulesRepository

    def create(self, schema: RulesSchema) -> Rules:
        rule = Rules(**schema.model_dump(exclude_none=True))
        return self.rulesRepository.create(rule)

    def delete(self, id: int) -> None:
        self.rulesRepository.delete(id)

    def get(self, id: int) -> Rules:
        return self.rulesRepository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Rules]:
        return self.rulesRepository.list(pageSize, startIndex)

    def update(self, id: int, schema: RulesSchema) -> Rules:
        rule = Rules(**schema.model_dump(exclude_none=True))
        return self.rulesRepository.update(id, rule)
