from typing import List

from sqlalchemy.orm import Session

from backend.models.competency import Competency
from backend.repositories.sql_alchemy.competency_repository import CompetencyRepository
from commons.interfaces.service import IService
from commons.models.core.competency import Competency as CompetencySchema


class CompetencyService(IService[Competency, CompetencySchema]):

    def __init__(self, db: Session) -> None:
        self.repository = CompetencyRepository(db)

    def create(self, schema: CompetencySchema) -> Competency:
        competency = Competency(**schema.model_dump(exclude_none=True))
        return self.repository.create(competency)

    def delete(self, id: id) -> None:
        self.repository.delete(id)

    def get(self, id: id) -> Competency:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Competency]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: id, schema: CompetencySchema) -> Competency:
        competency = Competency(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, competency)

    def bulk(self, schemas: List[CompetencySchema]) -> List[Competency]:
        schema_objects = [Competency(**schema.model_dump(exclude_none=True)) for schema in schemas]
        return self.repository.bulk(schema_objects)
