from typing import List

from sqlalchemy.orm import Session

from backend.interfaces.repository import IRepository
from backend.models.competency_level import CompetencyLevel


class CompetencyLevelRepository(IRepository[CompetencyLevel, id]):
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, instance: CompetencyLevel) -> CompetencyLevel:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, id: id) -> CompetencyLevel:
        return self.db.get(CompetencyLevel, id)

    def list(self, limit: int, start: int) -> List[CompetencyLevel]:
        return self.db.query(CompetencyLevel).offset(start).limit(limit).all()

    def update(self, id: id, instance: CompetencyLevel) -> CompetencyLevel:
        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance

    def delete(self, id: id) -> None:
        instance = self.get(id)
        if instance:
            self.db.delete(instance)
            self.db.commit()
