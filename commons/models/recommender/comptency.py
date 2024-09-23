from pydantic import Field

from commons.enum import Priority, Scope
from commons.models.base_dynamic_model import BaseDynamicModel


class CompetencyModelLLM(BaseDynamicModel):
    matching_competencies: str = Field(
        description="Competency that will be applied"
    )
    priority: Priority = Field(
        description="Priority that it is needed to learn this competency"
    )
    scope: Scope = Field(
        description="Scope that will be assigned to the competency to know better"
    )

    # Clase interna para la configuración del modelo
    class Config:
        json_schema_extra = {
            "example": {
                "matching_competencies": []
            }
        }
