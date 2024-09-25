from backend.models.competency import Competency
from backend.models.competency_level import CompetencyLevel
from backend.models.department import Department
from backend.repositories.sql_alchemy.competency_level_repository import CompetencyLevelRepository
from backend.repositories.sql_alchemy.competency_repository import CompetencyRepository
from backend.repositories.sql_alchemy.department_repository import DepartmenteRepository
from commons.enum import RequiredLevelEnum


def test_success_create_entity_object(test_get_db) -> None:
    department = Department(id=1, name="Defense Against the Dark Arts")
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.create(department)

    competencies = [Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
                Competency(id=2, name="Potions", description="Lorem Ipsum")]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    entity_model_def = CompetencyLevel(id=1,
                                       competency_id=1,
                                       department_id=1,
                                       required_level=RequiredLevelEnum.advanced.value,
                                       num_workers=5)
    repository=CompetencyLevelRepository(test_get_db)
    entity_def = entity_model_def
    entity = repository.create(entity_def)
    assert entity.num_workers == entity_def.num_workers


def test_success_list_entitys_objects(test_get_db) -> None:

    department = Department(id=1, name="Defense Against the Dark Arts")
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.create(department)

    competencies = [Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
                Competency(id=2, name="Potions", description="Lorem Ipsum")]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    entity_model_def = CompetencyLevel(id=1,
                                       competency_id=1,
                                       department_id=1,
                                       required_level=RequiredLevelEnum.advanced.value,
                                       num_workers=5)
    repository = CompetencyLevelRepository(test_get_db)
    repository.create(entity_model_def)
    entities = repository.list(limit=10, start=0)
    assert len(entities) == 1

def test_success_get_entitys_objects(test_get_db) -> None:

    department = Department(id=1, name="Defense Against the Dark Arts")
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.create(department)

    competencies = [Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
                Competency(id=2, name="Potions", description="Lorem Ipsum")]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    entity_model_def = CompetencyLevel(id=1,
                                       competency_id=1,
                                       department_id=1,
                                       required_level=RequiredLevelEnum.advanced.value,
                                       num_workers=5)
    repository = CompetencyLevelRepository(test_get_db)
    d = repository.create(entity_model_def)
    entity = repository.get(1)
    assert entity.num_workers == d.num_workers

def test_success_update_entity(test_get_db) -> None:

    department = Department(id=1, name="Defense Against the Dark Arts")
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.create(department)

    competencies = [Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
                Competency(id=2, name="Potions", description="Lorem Ipsum")]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    entity_model_def = CompetencyLevel(id=1,
                                       competency_id=1,
                                       department_id=1,
                                       required_level=RequiredLevelEnum.advanced.value,
                                       num_workers=5)
    repository = CompetencyLevelRepository(test_get_db)
    entity = repository.create(entity_model_def)
    entity.num_workers = 8
    entity_update = repository.update(entity.id, entity)
    assert entity_update.num_workers == entity.num_workers


def test_success_delete_entity(test_get_db) -> None:

    department = Department(id=1, name="Defense Against the Dark Arts")
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.create(department)

    competencies = [Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
                Competency(id=2, name="Potions", description="Lorem Ipsum")]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    entity_model_def = CompetencyLevel(id=1,
                                       competency_id=1,
                                       department_id=1,
                                       required_level=RequiredLevelEnum.advanced.value,
                                       num_workers=5)
    repository = CompetencyLevelRepository(test_get_db)
    created_entity = repository.create(entity_model_def)
    repository.delete(created_entity.id)
    entity = repository.get(1)
    assert entity is None

def test_success_bulk_entity_object(test_get_db) -> None:

    department = Department(id=1, name="Defense Against the Dark Arts")
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.create(department)

    competencies = [Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
                Competency(id=2, name="Potions", description="Lorem Ipsum")]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    list_entity_model_def = [CompetencyLevel(id=1,
                                       competency_id=1,
                                       department_id=1,
                                       required_level=RequiredLevelEnum.advanced.value,
                                       num_workers=5),
                   CompetencyLevel(id=2,
                                       competency_id=2,
                                       department_id=1,
                                       required_level=RequiredLevelEnum.intermediate.value,
                                       num_workers=8)]
    repository = CompetencyLevelRepository(test_get_db)
    entities = repository.bulk(list_entity_model_def)
    entities_list = repository.list(limit=10, start=0)
    assert len(entities) == len(entities_list)

def test_get_all_by_department(test_get_db) -> None:

    department = [Department(id=1, name="Defense Against the Dark Arts"),
                  Department(id=2, name="Wild and fantastic Animals")]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    competencies = [Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
                Competency(id=2, name="Potions", description="Lorem Ipsum")]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    list_entity_model_def = [CompetencyLevel(id=1,
                                       competency_id=1,
                                       department_id=1,
                                       required_level=RequiredLevelEnum.advanced.value,
                                       num_workers=5),
                   CompetencyLevel(id=2,
                                       competency_id=2,
                                       department_id=2,
                                       required_level=RequiredLevelEnum.intermediate.value,
                                       num_workers=8)]
    repository = CompetencyLevelRepository(test_get_db)
    repository.bulk(list_entity_model_def)

    dep_1 = repository.get_all_by_department(1)[0]
    dep_2 = repository.get_all_by_department(2)[0]

    assert dep_1["name"] == competencies[0].name
    assert dep_1["num_workers"] == list_entity_model_def[0].num_workers
    assert dep_1["required_level"] == list_entity_model_def[0].required_level
    assert dep_2["name"] == competencies[1].name
    assert dep_2["num_workers"] == list_entity_model_def[1].num_workers
    assert dep_2["required_level"] == list_entity_model_def[1].required_level
