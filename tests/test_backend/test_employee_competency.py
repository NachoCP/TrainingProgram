from backend.models.competency import Competency
from backend.models.department import Department
from backend.models.employee import Employee
from backend.models.employee_competency import EmployeeCompetency
from backend.models.employee_department import EmployeeDepartment
from backend.repositories.sql_alchemy.competency_repository import CompetencyRepository
from backend.repositories.sql_alchemy.department_repository import DepartmenteRepository
from backend.repositories.sql_alchemy.employee_competency_repository import EmployeeCompetencyRepository
from backend.repositories.sql_alchemy.employee_department_repository import EmployeeDepartmentRepository
from backend.repositories.sql_alchemy.employee_repository import EmployeeRepository
from commons.enum import RequiredLevelEnum


def test_success_create_entity_object(test_get_db) -> None:
    employee = [Employee(id=1, name="Gandalf the White"), Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    competencies = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    entity_model_def = EmployeeCompetency(
        id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value
    )
    repository = EmployeeCompetencyRepository(test_get_db)
    entity_def = entity_model_def
    entity = repository.create(entity_def)
    assert entity.current_level == entity_def.current_level


def test_success_list_entitys_objects(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"), Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    competencies = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    entity_model_def = EmployeeCompetency(
        id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value
    )
    repository = EmployeeCompetencyRepository(test_get_db)
    repository.create(entity_model_def)
    entities = repository.list(limit=10, start=0)
    assert len(entities) == 1


def test_success_get_entitys_objects(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"), Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    competencies = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    entity_model_def = EmployeeCompetency(
        id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value
    )
    repository = EmployeeCompetencyRepository(test_get_db)
    d = repository.create(entity_model_def)
    entity = repository.get(1)
    assert entity.current_level == d.current_level


def test_success_update_entity(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"), Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    competencies = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    entity_model_def = EmployeeCompetency(
        id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value
    )
    repository = EmployeeCompetencyRepository(test_get_db)
    entity = repository.create(entity_model_def)
    entity.current_level = RequiredLevelEnum.intermediate.value
    entity_update = repository.update(entity.id, entity)
    assert entity_update.current_level == entity.current_level


def test_success_delete_entity(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"), Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    competencies = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    entity_model_def = EmployeeCompetency(
        id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value
    )
    repository = EmployeeCompetencyRepository(test_get_db)
    created_entity = repository.create(entity_model_def)
    repository.delete(created_entity.id)
    entity = repository.get(1)
    assert entity is None


def test_success_bulk_entity_object(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"), Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    competencies = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    list_entity_model_def = [
        EmployeeCompetency(id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=2, employee_id=2, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
    ]
    repository = EmployeeCompetencyRepository(test_get_db)
    entities = repository.bulk(list_entity_model_def)
    entities_list = repository.list(limit=10, start=0)
    assert len(entities) == len(entities_list)


def test_success_get_all_by_department(test_get_db) -> None:

    department = [
        Department(id=1, name="Defense Against the Dark Arts"),
        Department(id=2, name="Wild and fantastic Animals"),
    ]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    employee = [
        Employee(id=1, name="Gandalf the White"),
        Employee(id=2, name="Saruman of Many Colours"),
        Employee(id=3, name="Radagast the Green"),
    ]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    employee_department = [
        EmployeeDepartment(id=1, employee_id=1, department_id=1),
        EmployeeDepartment(id=2, employee_id=2, department_id=1),
        EmployeeDepartment(id=3, employee_id=3, department_id=2),
    ]
    employee_department_repository = EmployeeDepartmentRepository(test_get_db)
    employee_department_repository.bulk(employee_department)

    competencies = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    list_entity_model_def = [
        EmployeeCompetency(id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=2, employee_id=2, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=3, employee_id=3, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
    ]
    repository = EmployeeCompetencyRepository(test_get_db)
    repository.bulk(list_entity_model_def)
    entities_list = repository.get_all_by_department(1)
    entities_list_2 = repository.get_all_by_department(2)
    assert len(entities_list) == 2
    assert entities_list[0]["employee_name"] == employee[0].name
    assert entities_list[1]["employee_name"] == employee[1].name
    assert entities_list[0]["competency_name"] == competencies[0].name
    assert entities_list[1]["required_level"] == list_entity_model_def[1].current_level
    assert len(entities_list_2) == 1
    assert entities_list[0]["employee_name"] == employee[0].name
    assert entities_list[0]["required_level"] == list_entity_model_def[0].current_level
    assert entities_list[0]["competency_name"] == competencies[0].name


def test_success_get_all_by_employee(test_get_db) -> None:

    employee = [
        Employee(id=1, name="Gandalf the White"),
        Employee(id=2, name="Saruman of Many Colours"),
        Employee(id=3, name="Radagast the Green"),
    ]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    competencies = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    list_entity_model_def = [
        EmployeeCompetency(id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=2, employee_id=1, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=3, employee_id=3, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
    ]
    repository = EmployeeCompetencyRepository(test_get_db)
    repository.bulk(list_entity_model_def)
    entities_list = repository.get_all_by_employee(1)

    assert len(entities_list) == 2
    assert entities_list[0]["name"] == competencies[0].name
    assert entities_list[1]["name"] == competencies[1].name
    assert entities_list[0]["current_level"] == list_entity_model_def[0].current_level
    assert entities_list[1]["current_level"] == list_entity_model_def[1].current_level
    assert len(repository.get_all_by_employee(2)) == 0
    assert len(repository.get_all_by_employee(3))


def test_success_group_competency_level_by_employee_ids(test_get_db) -> None:

    department = [
        Department(id=1, name="Defense Against the Dark Arts"),
        Department(id=2, name="Wild and fantastic Animals"),
    ]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    employee = [
        Employee(id=1, name="Gandalf the White"),
        Employee(id=2, name="Saruman of Many Colours"),
        Employee(id=3, name="Radagast the Green"),
    ]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    employee_department = [
        EmployeeDepartment(id=1, employee_id=1, department_id=1),
        EmployeeDepartment(id=2, employee_id=2, department_id=1),
        EmployeeDepartment(id=3, employee_id=3, department_id=2),
    ]
    employee_department_repository = EmployeeDepartmentRepository(test_get_db)
    employee_department_repository.bulk(employee_department)

    competencies = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    competencies_repository = CompetencyRepository(test_get_db)
    competencies_repository.bulk(competencies)

    list_entity_model_def = [
        EmployeeCompetency(id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=2, employee_id=2, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=3, employee_id=3, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
    ]
    repository = EmployeeCompetencyRepository(test_get_db)
    repository.bulk(list_entity_model_def)
    entities_list = repository.group_competency_level_by_employee_ids(1)
    entities_list_2 = repository.group_competency_level_by_employee_ids(2)
    assert len(entities_list) == 2
    assert entities_list[0]["name"] == "Dark Arts"
    assert entities_list[0]["required_level"] == RequiredLevelEnum.advanced.value
    assert entities_list[0]["num_workers"] == 1
    assert entities_list[1]["name"] == "Potions"
    assert len(entities_list_2) == 1
    assert entities_list_2[0]["name"] == "Potions"
