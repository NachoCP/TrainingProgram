from typing import Any, List

from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.competency import Competency
from backend.models.employee_competency import EmployeeCompetency
from backend.models.employee_department import EmployeeDepartment
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
        result = (self.db.query(Competency.name, EmployeeCompetency.current_level)
                  .join(Competency,Competency.id == EmployeeCompetency.competency_id)
                  .filter(EmployeeCompetency.employee_id==employee_id).all()
                  )
        result = [{"name": name, "required_level": required_level}
                  for name, required_level in result]
        return result

    def group_competency_level_by_employee_ids(self, department_id: int) -> List[Any]:
        result = (self.db.query(Competency.name, EmployeeCompetency.current_level,
                                func.count(EmployeeCompetency.id).label("num_workers"))
                  .join(Competency,Competency.id == EmployeeCompetency.competency_id)
                  .join(EmployeeDepartment, EmployeeCompetency.employee_id == EmployeeDepartment.department_id)
                  .filter(EmployeeDepartment.department_id == department_id)
                  .group_by(Competency.name, EmployeeCompetency.current_level)
                  .all())

        result = [{"name": name, "required_level": required_level, "num_workers": num_workers}
                  for name, required_level, num_workers in result]

        return result
