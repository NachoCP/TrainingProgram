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
COMPETENCY_PROMPT="commons/prompts/competency.prompt"
DEFAULT_LLM_MODEL="gpt-3.5-turbo"
DEFAULT_EMBEDDING_MODEL="text-embedding-3-small"
WEIGHTS_SCORING = {
        "coeff_priority": 0.30,
        "matching_competencies": 0.30,
        "matching_skills": 0.20,
        "rating": 0.10,
        "number_of_viewers": 0.10
    }
SEARCH_PARAMS = {"metric_type": "IP", "params": {}}
COURSE_DEFAULT_DIR_DATA="sample/online_courses_clean.json"
SYSTEM_MESSAGE_SYNTHETIC=("You are a world class AI that excels at generating synthetic data."
                       "Make sure to create the perfect number of entities")
SYSTEM_MESSAGE_COURSE=("You are a world class AI that excels at identifying topics in text description"
                       "You are about to be given a list of competencies as topics and a text snippet describing a course "
                       "and asked to identify which competencies are present in the course."
                       "Make sure to chose only competencies that are present in the list.")
SYSTEM_MESSAGE_COMPETENCY=("You are a world class AI that excel at detecting competencies to be improve by a person"
                       "You are about to be given a list of competencies as the pattern and a text snippet describing an employee performance which "
                       "will include feedback review and the needs of the company for its department (Competency, Number of workers needed)"
                       "Your task is to identify which competenies needs to be improved by the employee."
                       "Provide them ordered by priority"
                       "Make sure to chose only competencies that are present in the list."
                       "All the competency needed by the company should always be returned")
MAX_PRIORITY=4
