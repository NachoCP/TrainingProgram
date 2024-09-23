from pydantic import Field

from commons.constants import MAX_PRIORITY
from commons.models.base_dynamic_model import BaseDynamicModel


class CompetencyModelLLM(BaseDynamicModel):
    matching_competencies: str = Field(
        description="Competency that will be applied"
    )
    priority: int = Field(
        description=("Priority that it is needed to learn this competency."
                    "There are four priority values: 1, 2, 3, ... "
                    f"Where {MAX_PRIORITY} is the maximum priority")
    )


    # Clase interna para la configuración del modelo
    class Config:
        json_schema_extra = {
            "example": {
                    "matching_competencies": "Leadership",
                    "priority": "high"
                }
        }
