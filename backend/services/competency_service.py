from typing import List

from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.interfaces.service import IService
from backend.models.competency import Competency
from backend.repositories.sql_alchemy.competency_repository import CompetencyRepository
from backend.schemas.competency import Competency as CompetencySchema


class CompetencyService(IService[Competency, CompetencySchema]):

    def __init__(self, db: Session) -> None:
        self.repository = CompetencyRepository(db)

    def create(self, schema: CompetencySchema) -> Competency:
        competency = Competency(**schema.model_dump(exclude_none=True))
        return self.repository.create(competency)

    def delete(self, id: UUID4) -> None:
        self.repository.delete(id)

    def get(self, id: UUID4) -> Competency:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Competency]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: UUID4, schema: CompetencySchema) -> Competency:
        competency = Competency(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, competency)
