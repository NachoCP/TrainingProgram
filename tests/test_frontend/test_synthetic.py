from collections import Counter

from frontend.synthetic.generation import (
    get_competency_levels,
    get_employee_competencies,
    get_employee_departments,
    get_feedbacks,
)


def test_get_employee_competencies():

    comptency_ids_template = [1, 2]
    employee_ids_template = [1, 2, 3, 4, 5]

    employee_competencies = get_employee_competencies(employee_ids_template, comptency_ids_template)
    competency_ids = Counter([item.competency_id for item in employee_competencies])
    employee_ids = Counter([item.employee_id for item in employee_competencies])
    assert len(employee_competencies) == len(comptency_ids_template) * len(employee_ids_template)
    assert len(competency_ids) == len(comptency_ids_template)
    assert len(employee_ids) == len(employee_ids_template)

def test_get_employee_departments():

    departments_ids_template = [1, 2, 3]
    employee_ids_template = [1, 2, 3, 4, 5, 6]

    employee_departments = get_employee_departments(departments_ids_template, employee_ids_template)
    department_ids = Counter([item.department_id for item in employee_departments])
    employee_ids = Counter([item.employee_id for item in employee_departments])
    assert len(employee_departments) == len(employee_ids_template)
    assert len(department_ids) == len(department_ids)
    assert len(employee_ids) == len(employee_ids_template)

def test_get_competency_levels():

    departments_ids_template = [1, 2, 3]
    comptency_ids_template = [1, 2]

    competency_levels = get_competency_levels(comptency_ids_template, departments_ids_template, 10)

    assert len(competency_levels) == 10


def test_get_feedbacks():

    employee_ids_template = [1, 2, 3, 4, 5, 6]

    feedbacks = get_feedbacks(employee_ids_template, 6)

    assert len(feedbacks) == 6
