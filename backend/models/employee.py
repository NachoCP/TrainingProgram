import uuid

from sqlalchemy import UUID, Column, Date, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class Employee(EntityMeta):
    __tablename__ = "employee"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    hire_date = Column(Date, nullable=False)

    # Relationships
    competencies = relationship("EmployeeCompetency", back_populates="employee")
    departments = relationship("DepartmentEmployee", back_populates="employee")
