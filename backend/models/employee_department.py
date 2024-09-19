from sqlalchemy import Column, Date, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta
from backend.utils.vocabulary import RoleEnum


class EmployeeDepartment(EntityMeta):
    __tablename__ = "department_employee"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    expiration_date = Column(Date)
    effective_date = Column(Date, nullable=False)

    # Relationships
    employee = relationship("Employee", back_populates="departments")
    department = relationship("Department", back_populates="employees")
