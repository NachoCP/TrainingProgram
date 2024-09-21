import instructor
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

from recommender.llm.base_instructor import InstructorLLM

load_dotenv()


class OpenAIRunner(InstructorLLM):

    def __init__(self,
                 model: BaseModel,
                 llm_model_name: str = "gpt-3.5-turbo"):

        openai_client = instructor.from_openai(OpenAI())
        super().__init__(client=openai_client,
                       model=model,
                       llm_model_name=llm_model_name)

