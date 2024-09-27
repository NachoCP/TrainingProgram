from pydantic import Field

from commons.constants import MAX_PRIORITY
from commons.enum import PriorityType
from commons.models.base_dynamic_model import BaseDynamicModel


class CompetencyModelLLM(BaseDynamicModel):
    matching_competencies: str = Field(
        description=(
            "Identified competency for improvement by the employee."
            "Based on the detected text, the goal is to identify as many related competencies as possible."
        )
    )
    priority: int = (
        Field(
            description=(
                "Indicates the urgency of learning this competency, "
                f"with values ranging from 1 to {MAX_PRIORITY}, where {MAX_PRIORITY}"
                " represents the highest priority. Priority is determined by feedback,"
                " company requirements, and the department's gap from expected performance levels."
            )
        ),
    )
    competency_from: PriorityType = Field(
        description=("Indicates if the competency is coming from the feedback or the company")
    )

    # Clase interna para la configuración del modelo
    class Config:
        json_schema_extra = {"example": {}}
