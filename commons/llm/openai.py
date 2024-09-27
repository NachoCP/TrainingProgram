import instructor
from openai import OpenAI
from pydantic import BaseModel

from commons.config import get_environment_variables
from commons.llm.base_instructor import InstructorLLM

env = get_environment_variables()


class OpenAIRunner(InstructorLLM):

    def __init__(self, model: BaseModel, system_message: str):

        openai_client = instructor.from_openai(OpenAI(api_key=env.LLM_KEY))
        super().__init__(client=openai_client, model=model, system_message=system_message, llm_model_name=env.LLM_MODEL)
