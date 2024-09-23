from typing import List

from sqlalchemy.orm import Session

from backend.models.competency import Competency
from backend.models.competency_level import CompetencyLevel
from commons.interfaces.repository import IRepository


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

    def bulk(self, instances: List[CompetencyLevel]) -> List[CompetencyLevel]:

        self.db.bulk_save_objects(instances)
        self.db.commit()
        return instances

    def get_all_by_department(self, department_id: int) -> List[dict[str, str]]:
        competency_levels = (self.db.query(Competency.name, CompetencyLevel.required_level, CompetencyLevel.num_workers)
                             .join(Competency,CompetencyLevel.competency_id == Competency.id)
                             .filter(CompetencyLevel.department_id==department_id).all())

        result = [{"name": name, "required_level": required_level, "num_workers": num_workers}
                  for name, required_level, num_workers in competency_levels]

        return result
