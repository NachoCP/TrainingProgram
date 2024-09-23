import instructor
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

from commons.constants import DEFAULT_LLM_MODEL
from commons.llm.base_instructor import InstructorLLM

load_dotenv()


class OpenAIRunner(InstructorLLM):

    def __init__(self,
                 model: BaseModel,
                 system_message: str,
                 llm_model_name: str = DEFAULT_LLM_MODEL):

        openai_client = instructor.from_openai(OpenAI())
        super().__init__(client=openai_client,
                       model=model,
                       system_message=system_message,
                       llm_model_name=llm_model_name)

