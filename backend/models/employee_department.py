from sqlalchemy import Column, Date, ForeignKey, Integer, func
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class EmployeeDepartment(EntityMeta):
    __tablename__ = "employee_department"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False)
    expiration_date = Column(Date, nullable=True, default=None)
    effective_date = Column(Date, nullable=False, default=func.current_date())

    # Relationships
    employee = relationship("Employee", back_populates="employee_department")
    department = relationship("Department", back_populates="employee_department")
