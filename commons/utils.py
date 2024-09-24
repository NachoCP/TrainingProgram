import re
from pathlib import Path
from typing import Any, Dict, List

from commons.enum import RequiredLevelEnum


def read_text_file(path: str) -> str:
    """Helper function to read a prompt file based on the type."""
    return Path(path).read_text()

def identify_prompt_variables(text: str) -> list[str]:
    matches = re.findall(r"\{(.*?)\}", text)
    return matches


def preprocess_data(record: dict[str, Any]):
    # Replace None values with appropriate defaults
    record["title"] = record["title"] if record["title"] is not None else ""
    record["url"] = record["url"] if record["url"] is not None else ""
    record["short_intro"] = record["short_intro"] if record["short_intro"] is not None else ""
    record["category"] = record["category"] if record["category"] is not None else ""
    record["sub_category"] = record["sub_category"] if record["sub_category"] is not None else ""
    record["course_type"] = record["course_type"] if record["course_type"] is not None else ""
    record["language"] = record["language"] if record["language"] is not None else ""
    record["subtitle_languages"] = record["subtitle_languages"] if record["subtitle_languages"] is not None else ""
    record["skills"] = record["skills"] if record["skills"] is not None else ""
    record["instructors"] = record["instructors"] if record["instructors"] is not None else ""
    record["rating"] = record["rating"] if record["rating"] is not None else 0.0
    record["number_of_viewers"] = record["number_of_viewers"] if record["number_of_viewers"] is not None else 0.0
    record["site"] = record["site"] if record["site"] is not None else ""
    record["level"] = record["level"] if record["level"] is not None else ""
    record["number_of_reviews"] = record["number_of_reviews"] if record["number_of_reviews"] is not None else 0
    record["prequisites"] = record["prequisites"] if record["prequisites"] is not None else ""
    record["matching_competencies"] = ",".join(record["matching_competencies"]) if record["matching_competencies"] is not None else ""
    record["course_level"] = record["course_level"] if record["course_level"] is not None else ""

    return record


def normalize(list_values):
    min_value = min(list_values)
    max_value = max(list_values)
    return [(x - min_value) / (max_value - min_value) for x in list_values]



def merge_candidates_by_id(list1: List[Dict[str, Any]],
                                     list2: List[Dict[str, Any]],
                                     column_to_join: str) -> List[Dict[str, Any]]:

    merged_dict = {candidate['id']: candidate for candidate in list1}

    for candidate in list2:
        candidate_id = candidate['id']
        if candidate_id in merged_dict:
            merged_dict[candidate_id][column_to_join] = list(
                set(merged_dict[candidate_id].get(column_to_join, [])) | set(candidate.get(column_to_join, []))
            )
        else:
            merged_dict[candidate_id] = candidate

    return list(merged_dict.values())


def map_level_to_value(level):
    level_mapping = {
        RequiredLevelEnum.basic: 0,
        RequiredLevelEnum.intermediate: 1,
        RequiredLevelEnum.advanced: 2,
        RequiredLevelEnum.expert: 3
    }
    return level_mapping[level]
