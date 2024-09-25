from backend.models.employee import Employee
from backend.models.feedback import Feedback
from backend.repositories.sql_alchemy.employee_repository import EmployeeRepository
from backend.repositories.sql_alchemy.feedback_repository import FeedbackRepository


def test_success_create_entity_object(test_get_db) -> None:
    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    entity_model_def = Feedback(id=1, employee_id=1, feedback_by=2,
                                comments="I liked more the Grey one", score=3.1,
                                effective_date="2024-01-01")
    repository = FeedbackRepository(test_get_db)
    entity_def = entity_model_def
    entity = repository.create(entity_def)
    assert entity.comments == entity_def.comments


def test_success_list_entitys_objects(test_get_db) -> None:
    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    entity_model_def = Feedback(id=1, employee_id=1, feedback_by=2,
                                comments="I liked more the Grey one", score=3.1,
                                effective_date="2024-01-01")
    repository = FeedbackRepository(test_get_db)
    repository.create(entity_model_def)
    entities = repository.list(limit=10, start=0)
    assert len(entities) == 1

def test_success_get_entitys_objects(test_get_db) -> None:
    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    entity_model_def = Feedback(id=1, employee_id=1, feedback_by=2,
                                comments="I liked more the Grey one", score=3.1,
                                effective_date="2024-01-01")
    repository = FeedbackRepository(test_get_db)
    d = repository.create(entity_model_def)
    entity = repository.get(1)
    assert entity.comments == d.comments

def test_success_update_entity(test_get_db) -> None:
    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    entity_model_def = Feedback(id=1, employee_id=1, feedback_by=2,
                                comments="I liked more the Grey one", score=3.1,
                                effective_date="2024-01-01")
    repository = FeedbackRepository(test_get_db)
    entity = repository.create(entity_model_def)
    entity.comments = "I am unstopable"
    entity_update = repository.update(entity.id, entity)
    assert entity_update.comments == entity.comments


def test_success_delete_entity(test_get_db) -> None:
    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    entity_model_def = Feedback(id=1, employee_id=1, feedback_by=2,
                                comments="I liked more the Grey one", score=3.1,
                                effective_date="2024-01-01")
    repository = FeedbackRepository(test_get_db)
    created_entity = repository.create(entity_model_def)
    repository.delete(created_entity.id)
    entity = repository.get(1)
    assert entity is None

def test_success_bulk_entity_object(test_get_db) -> None:
    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours"),
                Employee(id=3, name="Radagast the Green")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    list_entity_model_def = [Feedback(id=1, employee_id=1, feedback_by=2,
                                comments="I liked more the Grey one", score=3.1,
                                effective_date="2024-01-01"),
                             Feedback(id=2, employee_id=1, feedback_by=3,
                                comments="I is a good guy", score=5.0,
                                effective_date="2024-01-02")]
    repository = FeedbackRepository(test_get_db)
    entities = repository.bulk(list_entity_model_def)
    entities_list = repository.list(limit=10, start=0)
    assert len(entities) == len(entities_list)
