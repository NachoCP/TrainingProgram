from typing import List

from pydantic import BaseModel

from commons.config import get_environment_variables
from commons.constants import SYNTHETHIC_PROMPT, SYSTEM_MESSAGE_SYNTHETIC
from commons.llm.factory import LLMProviderFactory
from commons.prompts.prompt_template import PromptTemplate

env = get_environment_variables()

class DataSyntheticLLM:

    def __init__(self,
                 model: BaseModel,
                 prompt_path: str = SYNTHETHIC_PROMPT,

                 ):

        self._llm_runner = LLMProviderFactory.get_provider(env.LLM_PROVIDER_MODEL)(model=List[model],
                                                                         system_message=SYSTEM_MESSAGE_SYNTHETIC)
        self._prompt = PromptTemplate(prompt_path)

    def create(self, num: int, preamble: str, **kwargs) -> List[BaseModel]:
        content = self._prompt.text(**{"num": num,
                                    "preamble": preamble})
        synthetic_data = self._llm_runner.run(content=content)

        return synthetic_data

