import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.fixtures import (
    competency,
    competency_level,
    course,
    department,
    employee,
    employee_competency,
    employee_department,
    feedback,
)


def test_success_return_status_code_201_recommend_course(
    client, employee, department, competency, employee_competency, employee_department, feedback, course
) -> None:
    test_client, _, _ = client

    response = test_client.get(f"api/v1/course/recommend_course/{employee[0].id}")
    assert response.status_code == 200
