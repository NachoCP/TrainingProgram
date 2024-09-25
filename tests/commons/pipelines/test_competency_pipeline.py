import pytest

from commons.enum import PriorityType, RequiredLevelEnum
from commons.models.core.competency import Competency
from commons.models.core.competency_level import CompetencyLevelEmployeeOutput, CompetencyLevelOutput
from commons.models.core.feedback import Feedback
from commons.pipelines.competency import CompetencyPipeline

competency_machine_learning = "Machine Learning Algorithms"
competency_creative_expression = "Creative Expression"

feedbacks = [
    Feedback(id=1,
             employee_id=1,
             feedback_by=1,
             comments="Your are bad at machine learning algorithms.",
             score="2.5",
             effective_date="2024-01-12")
]

competency_level_company = [
    CompetencyLevelOutput(name=competency_creative_expression,
                          required_level=RequiredLevelEnum.advanced,
                          num_workers=2)
]

competency_level_company_full = [
    CompetencyLevelOutput(name=competency_creative_expression,
                          required_level=RequiredLevelEnum.advanced,
                          num_workers=2),
    CompetencyLevelOutput(name=competency_machine_learning,
                        required_level=RequiredLevelEnum.advanced,
                        num_workers=2)
]

competency_level_department_matching = [
    CompetencyLevelOutput(name=competency_creative_expression,
                          required_level=RequiredLevelEnum.advanced,
                          num_workers=2),
    CompetencyLevelOutput(name=competency_machine_learning,
                        required_level=RequiredLevelEnum.advanced,
                        num_workers=2)
]

competency_level_department = [
    CompetencyLevelOutput(name=competency_creative_expression,
                          required_level=RequiredLevelEnum.basic,
                          num_workers=2),
    CompetencyLevelOutput(name=competency_machine_learning,
                        required_level=RequiredLevelEnum.basic,
                        num_workers=2)
]

competency_employee = [
    CompetencyLevelEmployeeOutput(name=competency_machine_learning, current_level=RequiredLevelEnum.basic),
    CompetencyLevelEmployeeOutput(name=competency_creative_expression, current_level=RequiredLevelEnum.basic)
    ]

competency_employee_advanced = [
    CompetencyLevelEmployeeOutput(name=competency_machine_learning, current_level=RequiredLevelEnum.advanced),
    CompetencyLevelEmployeeOutput(name=competency_creative_expression, current_level=RequiredLevelEnum.advanced)
    ]

competencies = [
    Competency(id=1, name=competency_creative_expression,
               description="The ability to express thoughts, emotions, and ideas creatively through written forms."),
    Competency(id=2, name=competency_machine_learning,
               description="Understanding and implementation of various machine learning algorithms for predictive modeling and problem-solving.")
]

def test_competency_pipeline_feedback():
    pipeline = CompetencyPipeline(competencies)
    priority = pipeline.transform(feedbacks, [], [], competency_employee)

    assert len(priority) == 1
    assert priority[0].competency_from == PriorityType.feedback
    assert priority[0].matching_competencies == competency_machine_learning

def test_competency_pipeline_rules():
    pipeline = CompetencyPipeline(competencies)
    priority = pipeline.transform([],
                                  competency_level_company,
                                  competency_level_department,
                                  competency_employee)

    assert len(priority) == 1
    assert priority[0].competency_from == PriorityType.company
    assert priority[0].matching_competencies == competency_creative_expression

def test_competency_pipeline_rules_non_priority():
    pipeline = CompetencyPipeline(competencies)
    priority = pipeline.transform([],
                                  competency_level_company,
                                  competency_level_department,
                                  competency_employee_advanced)

    assert len(priority) == 0

def test_competency_pipeline_rules_non_priority_company_requirements():
    pipeline = CompetencyPipeline(competencies)
    priority = pipeline.transform([],
                                  competency_level_company,
                                  competency_level_department_matching,
                                  competency_employee)

    assert len(priority) == 0

def test_competency_pipeline_full():
    pipeline = CompetencyPipeline(competencies)
    priority = pipeline.transform(feedbacks,
                                  competency_level_company_full,
                                  competency_level_department,
                                  competency_employee)

    expected_competencies = [competency_creative_expression, competency_machine_learning]
    assert len(priority) == 2
    assert sorted([p.matching_competencies for p in priority]) == expected_competencies
