import uuid

from sqlalchemy import UUID, Column, Date, ForeignKey, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class EmployeeCompetency(EntityMeta):
    __tablename__ = "employee_competency"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    employee_id = Column(UUID, ForeignKey("employee.id"), nullable=False)
    competency_id = Column(UUID, ForeignKey("competency.competency_id"), nullable=False)
    current_level = Column(String, nullable=False)
    assigned_date = Column(Date, nullable=False)

    # Relationships
    employee = relationship("Employee", back_populates="competencies")
    competency = relationship("Competency", back_populates="employees")
