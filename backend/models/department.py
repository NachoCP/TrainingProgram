from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class Department(EntityMeta):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    # Relationships
    employee_department = relationship("EmployeeDepartment", back_populates="department")
    competency_level = relationship("CompetencyLevel", back_populates="department")
