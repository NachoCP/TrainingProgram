from backend.models.department import Department
from backend.models.employee import Employee
from backend.models.employee_department import EmployeeDepartment
from backend.repositories.sql_alchemy.department_repository import DepartmenteRepository
from backend.repositories.sql_alchemy.employee_department_repository import EmployeeDepartmentRepository
from backend.repositories.sql_alchemy.employee_repository import EmployeeRepository


def test_success_create_entity_object(test_get_db) -> None:
    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    department = [Department(id=1, name="Defense Against the Dark Arts"),
                  Department(id=2, name="Wild and fantastic Animals")]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    entity_model_def = EmployeeDepartment(id=1, employee_id = 1, department_id=1)
    repository=EmployeeDepartmentRepository(test_get_db)
    entity_def = entity_model_def
    entity = repository.create(entity_def)
    assert entity.employee_id == entity_def.employee_id


def test_success_list_entitys_objects(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    department = [Department(id=1, name="Defense Against the Dark Arts"),
                  Department(id=2, name="Wild and fantastic Animals")]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    entity_model_def = EmployeeDepartment(id=1, employee_id = 1, department_id=1)
    repository=EmployeeDepartmentRepository(test_get_db)
    repository.create(entity_model_def)
    entities = repository.list(limit=10, start=0)
    assert len(entities) == 1

def test_success_get_entitys_objects(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    department = [Department(id=1, name="Defense Against the Dark Arts"),
                  Department(id=2, name="Wild and fantastic Animals")]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    entity_model_def = EmployeeDepartment(id=1, employee_id = 1, department_id=1)
    repository=EmployeeDepartmentRepository(test_get_db)
    d = repository.create(entity_model_def)
    entity = repository.get(1)
    assert entity.department_id == d.department_id

def test_success_update_entity(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    department = [Department(id=1, name="Defense Against the Dark Arts"),
                  Department(id=2, name="Wild and fantastic Animals")]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    entity_model_def = EmployeeDepartment(id=1, employee_id = 1, department_id=1)
    repository=EmployeeDepartmentRepository(test_get_db)
    entity = repository.create(entity_model_def)
    entity.employee_id = 2
    entity_update = repository.update(entity.id, entity)
    assert entity_update.employee_id == entity.employee_id


def test_success_delete_entity(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    department = [Department(id=1, name="Defense Against the Dark Arts"),
                  Department(id=2, name="Wild and fantastic Animals")]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    entity_model_def = EmployeeDepartment(id=1, employee_id = 1, department_id=1)
    repository=EmployeeDepartmentRepository(test_get_db)
    created_entity = repository.create(entity_model_def)
    repository.delete(created_entity.id)
    entity = repository.get(1)
    assert entity is None

def test_success_bulk_entity_object(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    department = [Department(id=1, name="Defense Against the Dark Arts"),
                  Department(id=2, name="Wild and fantastic Animals")]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    list_entity_model_def = [EmployeeDepartment(id=1, employee_id = 1, department_id=1),
                           EmployeeDepartment(id=2, employee_id = 2, department_id=1),
                           EmployeeDepartment(id=3, employee_id = 3, department_id=2)]
    repository=EmployeeDepartmentRepository(test_get_db)
    entities = repository.bulk(list_entity_model_def)
    entities_list = repository.list(limit=10, start=0)
    assert len(entities) == len(entities_list)

def test_success_get_all_by_department(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours"),
                Employee(id=3, name="Radagast the Green")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    department = [Department(id=1, name="Defense Against the Dark Arts"),
                  Department(id=2, name="Wild and fantastic Animals")]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    list_entity_model_def = [EmployeeDepartment(id=1, employee_id = 1, department_id=1),
                           EmployeeDepartment(id=2, employee_id = 2, department_id=1),
                           EmployeeDepartment(id=3, employee_id = 3, department_id=2)]
    repository=EmployeeDepartmentRepository(test_get_db)
    repository.bulk(list_entity_model_def)

    entities_list = repository.get_all_by_department(1)
    entities_list_2 = repository.get_all_by_department(2)

    assert len(entities_list) == 2
    assert entities_list[0]["name"] == employee[0].name
    assert entities_list[1]["name"] == employee[1].name
    assert len(entities_list_2) == 1
    assert entities_list_2[0]["name"] == employee[2].name

def test_success_get_id_by_employee_id(test_get_db) -> None:

    employee = [Employee(id=1, name="Gandalf the White"),
                Employee(id=2, name="Saruman of Many Colours"),
                Employee(id=3, name="Radagast the Green")]
    employee_repository = EmployeeRepository(test_get_db)
    employee_repository.bulk(employee)

    department = [Department(id=1, name="Defense Against the Dark Arts"),
                  Department(id=2, name="Wild and fantastic Animals")]
    department_repository = DepartmenteRepository(test_get_db)
    department_repository.bulk(department)

    list_entity_model_def = [EmployeeDepartment(id=1, employee_id = 1, department_id=1),
                           EmployeeDepartment(id=2, employee_id = 2, department_id=1),
                           EmployeeDepartment(id=3, employee_id = 3, department_id=2)]
    repository=EmployeeDepartmentRepository(test_get_db)
    repository.bulk(list_entity_model_def)

    assert repository.get_id_by_employee_id(1) == list_entity_model_def[0].department_id
    assert repository.get_id_by_employee_id(2) == list_entity_model_def[1].department_id
    assert repository.get_id_by_employee_id(3) == list_entity_model_def[2].department_id

