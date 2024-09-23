import json
from typing import Any

from pymilvus import MilvusClient

from backend.models.milvus.courses import get_course_schema
from commons.config import get_environment_variables
from commons.constants import COURSE_COLLECTION, COURSE_PROMPT, DEFAULT_EMBEDDING_MODEL, DEFAULT_LLM_MODEL
from commons.embeddings.factory import EmbeddingProviderFactory
from commons.enum import EmbeddingFactory, LLMFactory
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
                 llm_model: str =DEFAULT_LLM_MODEL,
                 llm_provider: str = LLMFactory.openai.value,
                 embedding_provider: str = EmbeddingFactory.openai.value,
                 embedding_model: str = DEFAULT_EMBEDDING_MODEL,
                 prompt_path: str = COURSE_PROMPT
                 ):

        dynamic_competencies = [c.name for c in competencies_data]
        CourseModelLLM.set_dynamic_example("matching_competencies", dynamic_competencies)

        self._competencies = '\n'.join([f"- {c.name}: {c.description}" for c in competencies_data])

        self._llm_model = llm_model
        self._llm_runner = LLMProviderFactory.get_provider(llm_provider)(CourseModelLLM)
        self._embeddign_runner = EmbeddingProviderFactory.get_provider(embedding_provider)(embedding_model, env.EMBEDDING_DIMENSION)
        self._prompt = PromptTemplate(prompt_path)
        self._milvus_client = MilvusClient(env.MILVUS_LITTLE)

    def extract(self, path) -> list[dict[str, Any]]:

        with open(path) as f:
            data_json = json.load(f)

        return data_json

    def transform(self,
                  data: list[Course],
                  **kwargs) -> Any:

        data_output = []
        batch = 0
        for course in data:
            input_text = (f"Title: {course['title']}, Category: {course['category']},"
                          f"Sub-Category: {course['sub_category']}, Short Intro: {course['short_intro']}"
                          f", Skills: {course['skills']}")
            content = self._prompt.text(**{"competencies": self._competencies,
                                     "courses": input_text})
            enrich_course = self._llm_runner.run(content=content)
            enrich_course = enrich_course.model_dump()

            if len(enrich_course["matching_competencies"]) == 0:
                continue
            enrich_course["embedding"] = self._embeddign_runner.get_embedding(','.join(enrich_course["matching_competencies"]))

            data_output.append(Course(**preprocess_data({**course, **enrich_course})))
            batch += 1

            if batch % 50 == 0:
                print(f"Number batch {batch}")
        return data_output

    def load(self,
             data: list[dict[str, Any]],
             **kwargs) -> Any:

        if not self._milvus_client.has_collection(COURSE_COLLECTION):
            self._milvus_client.create_collection(
                collection_name=COURSE_COLLECTION,
                schema=get_course_schema(env.EMBEDDING_DIMENSION)
            )

        self._milvus_client.insert(
            collection_name=COURSE_COLLECTION,
            data=data
        )

        #Create index after each load in order to refresh it
        index_params = self._milvus_client.prepare_index_params()
        index_params.add_index(
            field_name="embedding",
            metric_type="IP",
            index_type="FLAT",
            index_name="vector_index",
            params={ "nlist": 128 }
        )

        self._milvus_client.create_index(
            collection_name=COURSE_COLLECTION,
            index_params=index_params
        )
