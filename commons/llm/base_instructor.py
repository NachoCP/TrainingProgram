from typing import Any

from dotenv import load_dotenv
from pydantic import BaseModel

from commons.interfaces.llm import ILLM

load_dotenv()


class InstructorLLM(ILLM):

    def __init__(self,
                 client: Any,
                 model: BaseModel,
                 llm_model_name: str = "gpt-3.5-turbo"):

        self._client = client
        self._model = model
        self._llm_model_name = llm_model_name

    def run(self, **kwargs: Any) -> BaseModel:
        # Extract specific parameters from kwargs for flexibility
        content = kwargs.get("content", None)
        role = kwargs.get("role", "user")

        if not content:
            raise ValueError("The 'content' parameter is required and cannot be empty.")

        # Perform the API call
        return self._client.chat.completions.create(
            model=self._llm_model_name,
            response_model=self._model,
            messages=[
                {"role": role, "content": content},
            ],
        )
