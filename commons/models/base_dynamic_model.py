from typing import List

from pydantic import BaseModel


class BaseDynamicModel(BaseModel):

    class Config:
        json_schema_extra = {"example": {}}

    @classmethod
    def set_dynamic_example(cls, name_attribute: str, dynamic_values: List[str]):
        """Set dynamic examples for a given attribute."""
        cls.Config.json_schema_extra["example"][name_attribute] = dynamic_values
