import uuid

from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class Department(EntityMeta):
    __tablename__ = "department"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)

    # Relationships
    employees = relationship("EmployeeDepartment", back_populates="department")
