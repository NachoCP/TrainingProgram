from sqlalchemy import Column, Date, Integer, String, func
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class Employee(EntityMeta):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    expiration_date = Column(Date)
    effective_date = Column(Date, nullable=False, default=func.current_date())

    # Relationships
    employee_competency = relationship("EmployeeCompetency", back_populates="employee")
    employee_department = relationship("EmployeeDepartment", back_populates="employee")
