import os

from commons.utils import identify_prompt_variables, read_text_file


class PromptTemplate():

    def __init__(self, path: str):
        if not os.path.exists(path):
            raise ValueError(f"File does not exists {path}")
        self._prompt = read_text_file(path)
        self._variables = identify_prompt_variables(self._prompt)


    def text(self, **kwargs) -> str:
        for variable in self._variables:
            if variable not in kwargs.keys():
                raise AttributeError(f"Missing the following variable {variable}")

        formatted_prompt = self._prompt.format(**kwargs)

        return formatted_prompt
