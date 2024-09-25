import concurrent.futures
import json
from typing import Any, Dict, List

from commons.config import get_environment_variables
from commons.constants import (
    COURSE_PROMPT,
    SYSTEM_MESSAGE_COURSE,
)
from commons.embeddings.factory import EmbeddingProviderFactory
from commons.interfaces.pipeline import IPipeline
from commons.llm.factory import LLMProviderFactory
from commons.models.core.competency import Competency
from commons.models.core.course import Course
from commons.models.recommender.course import CourseModelLLM
from commons.prompts.prompt_template import PromptTemplate
from commons.utils import preprocess_data

env = get_environment_variables()


class CoursePipeline(IPipeline):

    def __init__(self,
                 competencies_data: list[Competency],
                 prompt_path: str = COURSE_PROMPT
                 ):

        dynamic_competencies = [c.name for c in competencies_data]
        CourseModelLLM.set_dynamic_example("matching_competencies", dynamic_competencies)
        self._competencies = '\n'.join([f"- {c.name}: {c.description}" for c in competencies_data])
        self._llm_runner = LLMProviderFactory.get_provider(env.LLM_PROVIDER_MODEL)(model=CourseModelLLM,
                                                                         system_message=SYSTEM_MESSAGE_COURSE)
        self._embeddign_runner = EmbeddingProviderFactory.get_provider(env.EMBEDDING_PROVIDER_MODEL)()
        self._prompt = PromptTemplate(prompt_path)
        self._parallel_processing = 10

    def extract(self, path) -> list[dict[str, Any]]:

        with open(path) as f:
            data_json = json.load(f)

        return data_json

    def transform(self,
                  data: List[Dict[str, str]],
                  **kwargs) -> List[Course]:

        data_output = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self._parallel_processing) as executor:
            futures = [executor.submit(self._enrich_course, course) for course in data]
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    data_output.append(result)
                except Exception as exc:
                    print(f"Generated an exception: {exc}")
                    raise exc
        return data_output

    def _enrich_course(self,
                       course: dict[str, str]) -> Course:

        input_text = (f"Title: {course['title']}, Category: {course['category']},"
                          f"Sub-Category: {course['sub_category']}, Short Intro: {course['short_intro']}"
                          f", Skills: {course['skills']}")
        content = self._prompt.text(**{"competencies": self._competencies,
                                    "courses": input_text})
        enrich_course = self._llm_runner.run(content=content)
        enrich_course = enrich_course.model_dump()

        if len(enrich_course["matching_competencies"]) == 0:
            return None
        enrich_course["embedding"] = self._embeddign_runner.get_embedding(','.join(enrich_course["matching_competencies"]))

        return Course(**preprocess_data({**course, **enrich_course}))

