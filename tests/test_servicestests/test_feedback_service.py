import os
import sys

from commons.models.core.feedback import Feedback

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.fixtures import (
    competency,
    competency_level,
    course,
    department,
    employee,
    feedback,
)


def test_success_return_status_code_201_create(client, employee) -> None:
    test_client, _, _ = client

    entity = Feedback(
        id=1,
        employee_id=1,
        feedback_by=2,
        comments="He should improve in Potions",
        score=3.1,
        effective_date="2024-01-01",
    )

    response = test_client.post(
        "api/v1/feedback",
        json=entity.model_dump(),
    )
    assert response.status_code == 201


def test_success_return_status_code_200_list(client, employee, feedback) -> None:
    test_client, _, _ = client

    response = test_client.get("api/v1/feedback")
    assert response.status_code == 202


def test_success_return_status_code_204_delete(client, employee, feedback) -> None:
    test_client, _, _ = client

    response = test_client.delete(f"api/v1/feedback/id/{feedback[0].id}")
    assert response.status_code == 204


def test_success_return_status_code_202_update(client, employee, feedback) -> None:
    test_client, _, _ = client

    entity = Feedback(
        id=1,
        employee_id=1,
        feedback_by=2,
        comments="He should improve in Potions",
        score=3.1,
        effective_date="2024-01-01",
    )
    response = test_client.put(f"api/v1/feedback/id/{feedback[0].id}", json=entity.model_dump())
    assert response.status_code == 202


def test_success_return_status_code_201_bulk(client, employee) -> None:
    test_client, _, _ = client

    entity = [
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
            score=4.0,
            effective_date="2024-01-02",
        ),
    ]
    response = test_client.post("api/v1/feedback/bulk", json=[e.model_dump() for e in entity])
    assert response.status_code == 201


def test_success_return_status_code_200_get_all_by_employee(client, employee, feedback) -> None:
    test_client, _, _ = client

    response = test_client.get(f"api/v1/feedback/employee/{employee[0].id}")
    assert response.status_code == 200
