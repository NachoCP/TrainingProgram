from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class Employee(EntityMeta):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    hire_date = Column(Date, nullable=False)

    # Relationships
    competencies = relationship("EmployeeCompetency", back_populates="employee")
    departments = relationship("EmployeeDepartment", back_populates="employee")
