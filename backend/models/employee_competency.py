from sqlalchemy import Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class EmployeeCompetency(EntityMeta):
    __tablename__ = "employee_competency"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
    competency_id = Column(Integer, ForeignKey("competency.id"), nullable=False)
    current_level = Column(String, nullable=False)
    expiration_date = Column(Date)
    effective_date = Column(Date, nullable=False, default=func.current_date())

    # Relationships
    employee = relationship("Employee", back_populates="employee_competency")
    competency = relationship("Competency", back_populates="employee_competency")
