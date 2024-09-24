import json
from typing import Any, List

from commons.config import get_environment_variables
from commons.constants import COMPETENCY_PROMPT, DEFAULT_LLM_MODEL, SYSTEM_MESSAGE_COMPETENCY
from commons.enum import LLMFactory
from commons.interfaces.pipeline import IPipeline
from commons.llm.factory import LLMProviderFactory
from commons.models.core.competency import Competency
from commons.models.core.competency_level import CompetencyLevelEmployeeOutput, CompetencyLevelOutput
from commons.models.core.feedback import Feedback
from commons.models.recommender.comptency import CompetencyModelLLM
from commons.prompts.prompt_template import PromptTemplate

env = get_environment_variables()


class CompetencyPipeline(IPipeline):

    def __init__(self,
                 competencies_data: list[Competency],
                 llm_model: str =DEFAULT_LLM_MODEL,
                 llm_provider: str = LLMFactory.openai.value):

        dynamic_competencies = [c.name for c in competencies_data]
        CompetencyModelLLM.set_dynamic_example("matching_competencies", dynamic_competencies)

        self._llm_model = llm_model
        self._llm_runner = LLMProviderFactory.get_provider(llm_provider)(List[CompetencyModelLLM],
                                                                         SYSTEM_MESSAGE_COMPETENCY)
        self._prompt = PromptTemplate(COMPETENCY_PROMPT)

    def extract(self, path) -> list[dict[str, Any]]:

        with open(path) as f:
            data_json = json.load(f)

        return data_json

    def transform(self,
                  feedback_reviews: List[Feedback],
                  company_competency_level: List[CompetencyLevelOutput],
                  department_competency_level: List[CompetencyLevelOutput],
                  employee_competency: List[CompetencyLevelEmployeeOutput],
                  **kwargs) -> List[CompetencyModelLLM]:

        feedback_reviews = "\n".join([f"- Score: {feedback.score}, Comments: {feedback.comments}" for feedback in feedback_reviews])

        competency_level_text = "\n".join([f"- Competency: {company_competency.name}, Level: {company_competency.required_level.value}, Num_workers: {company_competency.num_workers}"
                                      for company_competency in company_competency_level])

        department_competency_level_text = "\n".join([f"- Competency: {company_competency.name}, Level: {company_competency.required_level.value}, Num_workers: {company_competency.num_workers}"
                                      for company_competency in department_competency_level])

        employee_competency_text = "\n".join([f"- Competency: {company_competency.name}, Level: {company_competency.current_level.value}"
                                      for company_competency in employee_competency])


        content = self._prompt.text(**{"feedback_reviews": feedback_reviews,
                                       "competency_level_text": competency_level_text,
                                       "department_competency_level_text": department_competency_level_text,
                                       "employee_competency_text": employee_competency_text
                                       })
        competencies_output = self._llm_runner.run(content=content)
#
        return competencies_output
