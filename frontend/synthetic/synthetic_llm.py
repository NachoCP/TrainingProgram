from typing import List

from pydantic import BaseModel

from commons.constants import DEFAULT_LLM_MODEL, SYNTHETHIC_PROMPT
from commons.enum import LLMFactory
from commons.llm.factory import LLMProviderFactory
from commons.prompts.prompt_template import PromptTemplate


class DataSyntheticLLM:

    def __init__(self,
                 model: BaseModel,
                 llm_model: str =DEFAULT_LLM_MODEL,
                 llm_provider: str = LLMFactory.openai.value,
                 prompt_path: str = SYNTHETHIC_PROMPT,

                 ):

        self._llm_model = llm_model
        self._llm_runner = LLMProviderFactory.get_provider(llm_provider)(List[model])
        self._prompt = PromptTemplate(prompt_path)

    def create(self, num: int, preamble: str, **kwargs) -> List[BaseModel]:
        content = self._prompt.text(**{"num": num,
                                    "preamble": preamble})
        synthetic_data = self._llm_runner.run(content=content)

        return synthetic_data

