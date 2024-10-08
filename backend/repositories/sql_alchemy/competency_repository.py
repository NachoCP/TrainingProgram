from typing import List

from sqlalchemy.orm import Session

from backend.models.competency import Competency
from commons.interfaces.repository import IRepository


class CompetencyRepository(IRepository[Competency, id]):
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, instance: Competency) -> Competency:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, id: id) -> Competency:
        return self.db.get(Competency, id)

    def list(self, limit: int, start: int) -> List[Competency]:
        return self.db.query(Competency).offset(start).limit(limit).all()

    def update(self, id: id, instance: Competency) -> Competency:
        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance

    def delete(self, id: id) -> None:
        instance = self.get(id)
        if instance:
            self.db.delete(instance)
            self.db.commit()

    def bulk(self, instances: List[Competency]) -> List[Competency]:

        self.db.bulk_save_objects(instances)
        self.db.commit()
        return instances
