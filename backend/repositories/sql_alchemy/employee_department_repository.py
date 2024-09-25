from typing import List

from sqlalchemy.orm import Session

from backend.models.employee import Employee
from backend.models.employee_department import EmployeeDepartment
from commons.interfaces.repository import IRepository


class EmployeeDepartmentRepository(IRepository[EmployeeDepartment, id]):
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, instance: EmployeeDepartment) -> EmployeeDepartment:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, id: id) -> EmployeeDepartment:
        return self.db.get(EmployeeDepartment, id)

    def list(self, limit: int, start: int) -> List[EmployeeDepartment]:
        return self.db.query(EmployeeDepartment).offset(start).limit(limit).all()

    def update(self, id: id, instance: EmployeeDepartment) -> EmployeeDepartment:
        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance

    def delete(self, id: id) -> None:
        instance = self.get(id)
        if instance:
            self.db.delete(instance)
            self.db.commit()

    def bulk(self, instances: List[EmployeeDepartment]) -> List[EmployeeDepartment]:

        self.db.bulk_save_objects(instances)
        self.db.commit()
        return instances

    def get_all_by_department(self, department_id: int) -> List[dict[str, str]]:
        departments = (self.db.query(Employee.name, Employee.id)
                             .join(EmployeeDepartment,Employee.id == EmployeeDepartment.employee_id)
                             .filter(EmployeeDepartment.department_id==department_id).all())

        result = [{"name": name, "id": id}
                  for name, id in departments]

        return result

    def get_id_by_employee_id(self, employee_id: int) -> int:
        department_id = (self.db.query(EmployeeDepartment.department_id)
                       .filter_by(employee_id=employee_id)
                       .first())

        return department_id[0]
