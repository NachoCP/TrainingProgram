import uuid

from sqlalchemy import UUID, Column, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta
from backend.utils.vocabulary import RoleEnum


class EmployeeDepartment(EntityMeta):
    __tablename__ = "department_employee"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    employee_id = Column(UUID, ForeignKey("employee.id"), nullable=False)
    department_id = Column(UUID, ForeignKey("department.id"), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    expiration_date = Column(Date)
    effective_date = Column(Date, nullable=False)

    # Relationships
    employee = relationship("Employee", back_populates="departments")
    department = relationship("Department", back_populates="employees")
