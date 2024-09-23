from typing import Any, List

from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.competency import Competency
from backend.models.employee_competency import EmployeeCompetency
from commons.interfaces.repository import IRepository


class EmployeeCompetencyRepository(IRepository[EmployeeCompetency, id]):
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, instance: EmployeeCompetency) -> EmployeeCompetency:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, id: id) -> EmployeeCompetency:
        return self.db.get(EmployeeCompetency, id)

    def list(self, limit: int, start: int) -> List[EmployeeCompetency]:
        return self.db.query(EmployeeCompetency).offset(start).limit(limit).all()

    def update(self, id: id, instance: EmployeeCompetency) -> EmployeeCompetency:
        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance

    def delete(self, id: id) -> None:
        instance = self.get(id)
        if instance:
            self.db.delete(instance)
            self.db.commit()

    def bulk(self, instances: List[EmployeeCompetency]) -> List[EmployeeCompetency]:

        self.db.bulk_save_objects(instances)
        self.db.commit()
        return instances

    def get_all_by_employee(self, employee_id: int) -> List[EmployeeCompetency]:
        feedbacks = self.db.query(EmployeeCompetency).filter_by(employee_id=employee_id).all()
        return feedbacks

    def group_competency_level_by_employee_ids(self, employee_ids: List[int]) -> List[Any]:
        result = (self.db.query(Competency.name, EmployeeCompetency.current_level,
                                func.count(EmployeeCompetency.id).label("num_employees"))
                  .join(Competency,Competency.id == EmployeeCompetency.competency_id)
                  .filter(EmployeeCompetency.employee_id.in_(employee_ids))
                  .group_by(EmployeeCompetency.competency_id, EmployeeCompetency.current_level)
                  .all())
        return result
