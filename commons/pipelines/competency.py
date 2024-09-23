import concurrent.futures
import json
from typing import Any, List

from commons.config import get_environment_variables
from commons.constants import COMPETENCY_PROMPT, DEFAULT_LLM_MODEL
from commons.enum import LLMFactory
from commons.interfaces.pipeline import IPipeline
from commons.llm.factory import LLMProviderFactory
from commons.models.core.competency import Competency as CompetencyOutput
from commons.models.core.competency_level import CompetencyLevel
from commons.models.core.employee_competency import EmployeeCompetency
from commons.models.core.feedback import Feedback
from commons.prompts.prompt_template import PromptTemplate

env = get_environment_variables()


class CompetencyPipeline(IPipeline):

    def __init__(self,
                 llm_model: str =DEFAULT_LLM_MODEL,
                 llm_provider: str = LLMFactory.openai.value,
                 prompt_path: str = COMPETENCY_PROMPT
                 ):


        self._llm_model = llm_model
        self._llm_runner = LLMProviderFactory.get_provider(llm_provider)(List[str])
        self._prompt = PromptTemplate(prompt_path)

    def extract(self, path) -> list[dict[str, Any]]:

        with open(path) as f:
            data_json = json.load(f)

        return data_json

    def transform(self,
                  feedback_reviews: List[Feedback],
                  competency_level: List[CompetencyLevel],
                  deparmtnet_competency_status: List[dict[str, str]],
                  employee_competencies: List[EmployeeCompetency],
                  **kwargs) -> List[CompetencyOutput]:

        feedback_to_text = "\n".join([f"- Score: {feedback.score} Comments: {feedback.comments}" for feedback in feedback_reviews])
        feedback_reviews = f"This is the list of the feedback reviews from the empyloyee: \n {feedback_to_text}"
        data_output = []
        competency_level = "\n".join([f"-"])
            #for course in data:
        #    input_text = (f"Title: {course['title']}, Category: {course['category']},"
        #                  f"Sub-Category: {course['sub_category']}, Short Intro: {course['short_intro']}"
        #                  f", Skills: {course['skills']}")
        #    content = self._prompt.text(**{"competencies": self._competencies,
        #                             "courses": input_text})
        #    enrich_course = self._llm_runner.run(content=content)
        #    enrich_course = enrich_course.model_dump()
#
        #    if len(enrich_course["matching_competencies"]) == 0:
        #        continue
        #    enrich_course["embedding"] = self._embeddign_runner.get_embedding(','.join(enrich_course["matching_competencies"]))
#
        #    data_output.append(Course(**preprocess_data({**course, **enrich_course})))
        #    batch += 1
#
        #    if batch % 50 == 0:
        #        print(f"Number batch {batch}")
        return data_output
