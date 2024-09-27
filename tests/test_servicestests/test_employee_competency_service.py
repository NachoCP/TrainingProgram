import os
import sys

from commons.enum import RequiredLevelEnum
from commons.models.core.employee_competency import EmployeeCompetency

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.test_servicestests.fixtures import (
    competency,
    competency_level,
    course,
    department,
    employee,
    employee_competency,
    employee_department,
    feedback,
)


def test_success_return_status_code_201_create(client, employee, competency) -> None:
    test_client, _, _ = client

    entity = EmployeeCompetency(id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value)

    response = test_client.post(
        "api/v1/employee_competency",
        json=entity.model_dump(),
    )
    assert response.status_code == 201


def test_success_return_status_code_200_list(client, employee, competency, employee_competency) -> None:
    test_client, _, _ = client

    response = test_client.get("api/v1/employee_competency")
    assert response.status_code == 200


def test_success_return_status_code_204_delete(client, employee, department, employee_department) -> None:
    test_client, _, _ = client

    response = test_client.delete(f"api/v1/employee_competency/id/{department[0].id}")
    assert response.status_code == 204


def test_success_return_status_code_202_update(client, employee, department, employee_department) -> None:
    test_client, _, _ = client

    entity = EmployeeCompetency(id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value)
    response = test_client.put(f"api/v1/employee_competency/id/{department[0].id}", json=entity.model_dump())
    assert response.status_code == 202


def test_success_return_status_code_201_bulk(client) -> None:
    test_client, _, _ = client

    entity = [
        EmployeeCompetency(id=1, employee_id=1, competency_id=1, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=2, employee_id=2, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
        EmployeeCompetency(id=3, employee_id=3, competency_id=2, current_level=RequiredLevelEnum.advanced.value),
    ]
    response = test_client.post("api/v1/employee_competency/bulk", json=[e.model_dump() for e in entity])
    assert response.status_code == 201


def test_success_return_status_code_200_get_all_by_employee(
    client, employee, department, competency, employee_department, employee_competency
) -> None:
    test_client, _, _ = client

    response = test_client.get(f"api/v1/employee_competency/employee/{employee[0].id}")
    assert response.status_code == 200


def test_success_return_status_code_200_group_competency_level_by_employee_ids(
    client, employee, department, competency, employee_department, employee_competency
) -> None:
    test_client, _, _ = client

    response = test_client.get(f"api/v1/employee_competency/group/department/{department[0].id}")
    assert response.status_code == 200


def test_success_return_status_code_200_get_all_by_department(
    client, employee, department, competency, employee_department, employee_competency
) -> None:
    test_client, _, _ = client

    response = test_client.get(f"api/v1/employee_competency/department/{department[0].id}")
    assert response.status_code == 200
