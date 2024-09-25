import json
from typing import Any, List

import pandas as pd

from commons.config import get_environment_variables
from commons.constants import COMPETENCY_PROMPT, DEFAULT_LLM_MODEL, SYSTEM_MESSAGE_COMPETENCY
from commons.enum import LLMFactory, PriorityType, level_mapping
from commons.interfaces.pipeline import IPipeline
from commons.llm.factory import LLMProviderFactory
from commons.models.core.competency import Competency
from commons.models.core.competency_level import CompetencyLevelEmployeeOutput, CompetencyLevelOutput
from commons.models.core.feedback import Feedback
from commons.models.recommender.comptency import CompetencyModelLLM
from commons.prompts.prompt_template import PromptTemplate

env = get_environment_variables()


class CompetencyPipeline(IPipeline):

    def __init__(self,
                 competencies_data: list[Competency],
                 llm_model: str =DEFAULT_LLM_MODEL,
                 llm_provider: str = LLMFactory.openai.value):

        dynamic_competencies = [c.name for c in competencies_data]
        CompetencyModelLLM.set_dynamic_example("matching_competencies", dynamic_competencies)
        self._competencies = '\n'.join([f"- {c.name}" for c in competencies_data])
        self._llm_model = llm_model
        self._llm_runner = LLMProviderFactory.get_provider(llm_provider)(List[CompetencyModelLLM],
                                                                         SYSTEM_MESSAGE_COMPETENCY)
        self._prompt = PromptTemplate(COMPETENCY_PROMPT)

    def extract(self, path) -> list[dict[str, Any]]:

        with open(path) as f:
            data_json = json.load(f)

        return data_json

    def transform(self,
                  feedback_reviews: List[Feedback],
                  company_competency_level: List[CompetencyLevelOutput],
                  department_competency_level: List[CompetencyLevelOutput],
                  employee_competency: List[CompetencyLevelEmployeeOutput],
                  **kwargs) -> List[CompetencyModelLLM]:

        feedback_reviews = "\n".join([f"- Score: {feedback.score}, Comments: {feedback.comments}" for feedback in feedback_reviews])

        employee_competency_dict = {c.name: level_mapping[c.current_level] for c in employee_competency}
        df_competency_level = pd.DataFrame([d.model_dump() for d in company_competency_level])
        df_department_level = pd.DataFrame([d.model_dump() for d in department_competency_level])
        competency_levels = ""
        competency_names = {}
        if len(df_competency_level) > 0:
            df_merged_levels = df_competency_level.merge(df_department_level,
                                                        on=["name", "required_level"],
                                                        how="outer",
                                                        suffixes=('_expected', '_real'))
            df_merged_levels["num_workers_expected"] = df_merged_levels["num_workers_expected"].fillna(0)
            df_merged_levels["num_workers_real"] = df_merged_levels["num_workers_real"].fillna(0)
            df_merged_levels["diff_num_workers"] = (df_merged_levels["num_workers_real"] - df_merged_levels["num_workers_expected"]).astype(int)
            df_merged_levels["level_value"] = df_merged_levels["required_level"].map(level_mapping)
            df_merged_levels_filtered = pd.merge(df_merged_levels,
                                pd.DataFrame(list(employee_competency_dict.items()), columns=["name", "level_limit"]), on="name") \
                            .query("level_value > level_limit")
            df_merged_levels_filtered = df_merged_levels_filtered[df_merged_levels_filtered["diff_num_workers"].astype(int) < 0]
            df_merged_level_results = df_merged_levels_filtered.groupby("name")["diff_num_workers"].sum()

            competency_levels = "\n".join([f"- Competency: {name}, Workers_needed: {abs(diff)}" for name, diff in df_merged_level_results.items()])
            competency_names = {name for name, _ in df_merged_level_results.items()}

        content = self._prompt.text(**{"feedback_reviews": feedback_reviews,
                                       "competencies": self._competencies,
                                       "competency__levels": competency_levels
                                       })

        if (len(feedback_reviews) == 0 and len(competency_names) == 0):
            return []
        competencies_output = self._llm_runner.run(content=content)

        for competency_output in competencies_output:
            if len(feedback_reviews) == 0:
                competency_output.competency_from = PriorityType.company
            elif competency_output.matching_competencies in competency_names:
                competency_output.competency_from = PriorityType.both
            else:
                competency_output.competency_from = PriorityType.feedback

        return competencies_output
