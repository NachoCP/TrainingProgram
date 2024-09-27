import random
from typing import List

from commons.enum import RequiredLevelEnum
from commons.models.core.competency_level import CompetencyLevel
from commons.models.core.employee_competency import EmployeeCompetencyWithoutDates
from commons.models.core.employee_department import EmployeeDepartmentWithoutDates
from commons.models.core.feedback import Feedback
from frontend.synthetic.synthetic_llm import DataSyntheticLLM


def get_feedbacks(employee_ids: List[int], num: int = 40) -> List[Feedback]:

    preamble = (
        "The following list of ids are from all the employees of the company."
        "Used them to generate the feedback from and to. Try to give equal reviews positive and negative"
        "Do not use other ids rather than the others provided"
        "Generate at least 60% negative reviews"
        f"List of ids: {employee_ids}"
    )
    data = DataSyntheticLLM(Feedback).create(num=num, preamble=preamble)
#    data.extend(DataSyntheticLLM(Feedback).create(num=30, preamble=preamble))
    index = 0
    for d in data:
        d.id = index
        index += 1
    return data


def get_competency_levels(competency_ids: List[int], department_ids: List[int], num:int = 40) -> List[CompetencyLevel]:
    preamble = (
        "You are going to be provided with two list: competencies and departments."
        "Used them to generate the rules to set up level of competencies between the different departments"
        "Try to generate them equally and dont set up to many rules for expert"
        "There is no need for basic levels"
        f"List of departments: {department_ids}"
        f"List of competencies: {competency_ids}"
    )

    data = DataSyntheticLLM(CompetencyLevel).create(num=num, preamble=preamble)
    return data


def get_employee_departments(
    department_ids: List[int], employee_ids: List[int]
) -> List[EmployeeDepartmentWithoutDates]:
    department_assignments = []
    index = 1
    for i, employee in enumerate(employee_ids):
        department_index = i % len(department_ids)
        department_assignments.append(
            EmployeeDepartmentWithoutDates(
                id=index, employee_id=employee, department_id=department_ids[department_index]
            )
        )
        index += 1

    return department_assignments


def get_employee_competencies(
    employee_ids: List[int], competency_ids: List[int]
) -> List[EmployeeCompetencyWithoutDates]:

    def _assign_random_level():
        LEVEL_PROBABLITIES = {
            RequiredLevelEnum.basic: 0.4,
            RequiredLevelEnum.intermediate: 0.3,
            RequiredLevelEnum.advanced: 0.20,
            RequiredLevelEnum.expert: 0.1,
        }
        levels = list(LEVEL_PROBABLITIES.keys())
        probabilities = list(LEVEL_PROBABLITIES.values())
        return random.choices(levels, probabilities)[0]

    employee_competency_data = []
    id_num = 1
    for employee in employee_ids:
        for competency in competency_ids:
            level = _assign_random_level()
            employee_competency_data.append(
                EmployeeCompetencyWithoutDates(
                    id=id_num, employee_id=employee, competency_id=competency, current_level=level.value
                )
            )
            id_num += 1

    return employee_competency_data
