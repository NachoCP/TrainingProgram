from backend.config.database import engine
from backend.models.base import Base
from backend.models.competency import Competency
from backend.models.competency_level import CompetencyLevel
from backend.models.department import Department
from backend.models.employee import Employee
from backend.models.employee_competency import EmployeeCompetency
from backend.models.employee_department import EmployeeDepartment
from backend.models.feedback import Feedback


def create_tables():
    Base.metadata.create_all(bind=engine)
    Competency.metadata.create_all(bind=engine)
    Employee.metadata.create_all(bind=engine)
    Department.metadata.create_all(bind=engine)
    CompetencyLevel.metadata.create_all(bind=engine)
    EmployeeCompetency.metadata.create_all(bind=engine)
    EmployeeDepartment.metadata.create_all(bind=engine)
    Feedback.metadata.create_all(bind=engine)
