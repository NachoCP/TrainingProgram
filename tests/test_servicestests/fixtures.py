import pytest

from backend.models.competency import Competency
from backend.models.competency_level import CompetencyLevel
from backend.models.department import Department
from backend.models.employee import Employee
from backend.models.employee_competency import EmployeeCompetency
from backend.models.employee_department import EmployeeDepartment
from backend.models.feedback import Feedback
from backend.repositories.milvus.course_repository import CourseRepository
from backend.repositories.sql_alchemy.competency_level_repository import CompetencyLevelRepository
from backend.repositories.sql_alchemy.competency_repository import CompetencyRepository
from backend.repositories.sql_alchemy.department_repository import DepartmenteRepository
from backend.repositories.sql_alchemy.employee_competency_repository import EmployeeCompetencyRepository
from backend.repositories.sql_alchemy.employee_department_repository import EmployeeDepartmentRepository
from backend.repositories.sql_alchemy.employee_repository import EmployeeRepository
from commons.enum import RequiredLevelEnum
from commons.models.core.course import Course


@pytest.fixture(scope="function")
def employee(client):
    _, db_session, _ = client
    entity_model_def = [
        Employee(id=1, name="Gandalf the White"),
        Employee(id=2, name="Saruman of Many Colours"),
        Employee(id=3, name="Radagast the Green"),
    ]
    repository = EmployeeRepository(db_session)
    entity_def = entity_model_def
    entity = repository.bulk(entity_def)
    return entity


@pytest.fixture(scope="function")
def competency(client):
    _, db_session, _ = client
    entity_model_def = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    repository = CompetencyRepository(db_session)
    entity_def = entity_model_def
    entity = repository.bulk(entity_def)
    return entity


@pytest.fixture(scope="function")
def department(client):
    _, db_session, _ = client
    entity_model_def = [
        Department(id=1, name="Defense Against the Dark Arts"),
        Department(id=2, name="Wild and fantastic Animals"),
    ]
    repository = DepartmenteRepository(db_session)
    entity_def = entity_model_def
    entity = repository.bulk(entity_def)
    return entity


@pytest.fixture(scope="function")
def employee_department(client):
    _, db_session, _ = client
    entity_model_def = [
        EmployeeDepartment(id=1, employee_id=1, department_id=1),
        EmployeeDepartment(id=2, employee_id=2, department_id=1),
        EmployeeDepartment(id=3, employee_id=3, department_id=2),
    ]
    repository = EmployeeDepartmentRepository(db_session)
    entity_def = entity_model_def
    entity = repository.bulk(entity_def)
    return entity


@pytest.fixture(scope="function")
def employee_competency(client):
    _, db_session, _ = client
    entity_model_def = [
        EmployeeCompetency(id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=2, employee_id=2, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=3, employee_id=3, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
    ]
    repository = EmployeeCompetencyRepository(db_session)
    entity_def = entity_model_def
    entity = repository.bulk(entity_def)
    return entity


@pytest.fixture(scope="function")
def competency_level(client):
    _, db_session, _ = client
    entity_model_def = [
        CompetencyLevel(
            id=1, competency_id=1, department_id=1, required_level=RequiredLevelEnum.advanced.value, num_workers=5
        ),
        CompetencyLevel(
            id=2, competency_id=2, department_id=1, required_level=RequiredLevelEnum.intermediate.value, num_workers=8
        ),
    ]
    repository = CompetencyLevelRepository(db_session)
    entity_def = entity_model_def
    entity = repository.bulk(entity_def)
    return entity


@pytest.fixture(scope="function")
def feedback(client):
    _, db_session, _ = client
    entity_model_def = [
        Feedback(
            id=1,
            employee_id=1,
            feedback_by=2,
            comments="He should improve in Potions",
            score=3.1,
            effective_date="2024-01-01",
        ),
        Feedback(
            id=2,
            employee_id=1,
            feedback_by=3,
            comments="Very good at Defense against dark magic",
            score=4.9,
            effective_date="2024-01-02",
        ),
    ]
    repository = CompetencyLevelRepository(db_session)
    entity_def = entity_model_def
    entity = repository.bulk(entity_def)
    return entity


@pytest.fixture(scope="function")
def course(client):
    _, _, milvus_client = client
    course_1 = Course(
        title="Mastering the Dark Arts",
        url="https://example.com/dark-arts-course",
        short_intro="An advanced course on the forbidden arts of magic.",
        category="Magic",
        sub_category="Dark Arts",
        course_type="video",
        language="Ancient Runes",
        subtitle_languages="Parseltongue, Latin",
        skills="Curses, Hexes, Dark Spells",
        instructors="Lord Voldemort",
        rating=4.9,
        number_of_viewers=3500,
        site="Hogwarts Online",
        level="expert",
        number_of_reviews=1200,
        prequisites="Defense Against the Dark Arts",
        matching_competencies="Dark Arts",
        course_level="expert",
        embedding=[0.0] * 1536,
    )

    course_2 = Course(
        title="Advanced Potions Brewing",
        url="https://example.com/potions-course",
        short_intro="A deep dive into the art of brewing powerful potions.",
        category="Magic",
        sub_category="Potions",
        course_type="text",
        language="English",
        subtitle_languages="Latin, Gobbledegook",
        skills="Potion brewing, Ingredient mastery",
        instructors="Severus Snape",
        rating=4.8,
        number_of_viewers=4200,
        site="Hogwarts Online",
        level="advanced",
        number_of_reviews=1500,
        prequisites="Introduction to Potions",
        matching_competencies="Potions",
        course_level="advanced",
        embedding=[0.5] * 1536,
    )
    repository = CourseRepository(milvus_client)
    courses = repository.bulk([course_1, course_2])
    return courses
