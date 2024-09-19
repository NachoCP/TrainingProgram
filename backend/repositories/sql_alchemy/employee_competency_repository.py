from typing import List

from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.interfaces.repository import IRepository
from backend.models.employee_competency import EmployeeCompetency


class EmployeeCompetencyRepository(IRepository[EmployeeCompetency, UUID4]):
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, instance: EmployeeCompetency) -> EmployeeCompetency:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, id: UUID4) -> EmployeeCompetency:
        return self.db.get(EmployeeCompetency, id)

    def list(self, limit: int, start: int) -> List[EmployeeCompetency]:
        return self.db.query(EmployeeCompetency).offset(start).limit(limit).all()

    def update(self, id: UUID4, instance: EmployeeCompetency) -> EmployeeCompetency:
        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance

    def delete(self, id: UUID4) -> None:
        instance = self.get(id)
        if instance:
            self.db.delete(instance)
            self.db.commit()
