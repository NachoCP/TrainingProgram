from typing import List

from commons.config import get_environment_variables
from commons.constants import DEFAULT_LLM_MODEL, SYNTHETHIC_PROMPT
from commons.enum import LLMFactory
from commons.llm.factory import LLMProviderFactory
from commons.models.core.employee import Employee
from commons.prompts.prompt_template import PromptTemplate
from frontend.synthetic.synthetic_llm import ISyntheticService

env = get_environment_variables()


class EmployeeSyntheticService(ISyntheticService):

    def __init__(self,
                 llm_model: str =DEFAULT_LLM_MODEL,
                 llm_provider: str = LLMFactory.openai.value,
                 prompt_path: str = SYNTHETHIC_PROMPT
                 ):

        self._llm_model = llm_model
        self._llm_runner = LLMProviderFactory.get_provider(llm_provider)(List[Employee])
        self._prompt = PromptTemplate(prompt_path)

    def create(self, num: int, preamble: str, **kwargs) -> List[Employee]:
        content = self._prompt.text(**{"num": num,
                                    "preamble": preamble})
        synthetic_data = self._llm_runner.run(content=content)

        return synthetic_data

    def send(self, data: List[Employee]) -> None:

        pass
