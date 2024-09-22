COURSE_COLLECTION = "course_collection"
EMBEDDING_COLUMN = "embedding"
COURSE_OUTPUT_FIELDS = [
 "title",
 "url",
 "short_intro",
 "category",
 "sub_category",
 "course_type",
 "language",
 "subtitle_languages",
 "skills",
 "instructors",
 "rating",
 "number_of_viewers",
 "site",
 "level",
 "number_of_reviews",
 "matching_competencies",
 "prequisites"]

SYNTHETHIC_PROMPT="commons/prompts/synthetic_data.prompt"
COURSE_PROMPT="commons/prompts/course.prompt"
DEFAULT_LLM_MODEL="gpt-3.5-turbo"
DEFAULT_EMBEDDING_MODEL="text-embedding-3-small"
WEIGHTS_SCORING = {
        "matching_competencies": 0.30,
        "matching_skills": 0.30,
        "rating": 0.20,
        "number_of_reviews": 0.10,
        "number_of_viewers": 0.10
    }
SEARCH_PARAMS = {"metric_type": "IP", "params": {}}
