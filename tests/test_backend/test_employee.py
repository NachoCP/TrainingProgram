from backend.models.employee import Employee
from backend.repositories.sql_alchemy.employee_repository import EmployeeRepository


def test_success_create_entity_object(test_get_db) -> None:
    entity_model_def = Employee(id=1, name="Gandalf the White")
    repository = EmployeeRepository(test_get_db)
    entity_def = entity_model_def
    entity = repository.create(entity_def)
    assert entity.name == entity_def.name


def test_success_list_entitys_objects(test_get_db) -> None:
    entity_model_def = Employee(id=1, name="Gandalf the White")
    repository = EmployeeRepository(test_get_db)
    repository.create(entity_model_def)
    entities = repository.list(limit=10, start=0)
    assert len(entities) == 1


def test_success_get_entitys_objects(test_get_db) -> None:
    entity_model_def = Employee(id=1, name="Gandalf the White")
    repository = EmployeeRepository(test_get_db)
    d = repository.create(entity_model_def)
    entity = repository.get(1)
    assert entity.name == d.name


def test_success_update_entity(test_get_db) -> None:
    entity_model_def = Employee(id=1, name="Gandalf the Grey")
    repository = EmployeeRepository(test_get_db)
    entity = repository.create(entity_model_def)
    entity.name = "Gandalf the White"
    entity_update = repository.update(entity.id, entity)
    assert entity_update.name == entity.name


def test_success_delete_entity(test_get_db) -> None:
    entity_model_def = Employee(id=1, name="Gandalf the White")
    repository = EmployeeRepository(test_get_db)
    created_entity = repository.create(entity_model_def)
    repository.delete(created_entity.id)
    entity = repository.get(1)
    assert entity is None


def test_success_bulk_entity_object(test_get_db) -> None:
    list_entity_model_def = [Employee(id=1, name="Gandalf the White"), Employee(id=2, name="Harry Potter")]
    repository = EmployeeRepository(test_get_db)
    entities = repository.bulk(list_entity_model_def)
    entities_list = repository.list(limit=10, start=0)
    assert len(entities) == len(entities_list)
