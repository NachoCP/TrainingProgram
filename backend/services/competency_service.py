from typing import List

from backend.interfaces.service import IService
from backend.models.competency import Competency
from backend.repositories.sql_alchemy.competency_repository import CompetencyRepository
from backend.schemas.competency import Competency as CompetencySchema


class CompetencyService(IService[Competency, CompetencySchema]):
    def __init__(self, competencyRepository: CompetencyRepository) -> None:
        self.competencyRepository = competencyRepository

    def create(self, schema: CompetencySchema) -> Competency:
        competency = Competency(**schema.model_dump(exclude_none=True))
        return self.competencyRepository.create(competency)

    def delete(self, id: int) -> None:
        self.competencyRepository.delete(id)

    def get(self, id: int) -> Competency:
        return self.competencyRepository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Competency]:
        return self.competencyRepository.list(pageSize, startIndex)

    def update(self, id: int, schema: CompetencySchema) -> Competency:
        competency = Competency(**schema.model_dump(exclude_none=True))
        return self.competencyRepository.update(id, competency)
