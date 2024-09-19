from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class Department(EntityMeta):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    # Relationships
    employees = relationship("EmployeeDepartment", back_populates="department")
