from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class EmployeeCompetency(EntityMeta):
    __tablename__ = 'employee_competency'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    competency_id = Column(Integer, ForeignKey('competency.competency_id'), nullable=False)
    current_level = Column(String, nullable=False)
    assigned_date = Column(Date, nullable=False)

    # Relationships
    employee = relationship("Employee", back_populates="competencies")
    competency = relationship("Competency", back_populates="employees")
