from commons.models.core.competency import Competency
from commons.models.core.course import Course
from commons.pipelines.course import CoursePipeline

course_1 = {
    "title": "Introduction to Machine Learning",
    "category": "Technology",
    "sub_category": "Artificial Intelligence",
    "short_intro": "Learn the basics of machine learning algorithms and their real-world applications.",
    "skills": "Python, Data Science, Machine Learning, Linear Algebra",
    "url": "Testing",
    "course_type": "Testing",
    "language": "lang",
    "subtitle_languages": "lang",
    "instructors": "Testing N",
    "rating": None,
    "level": "Advanced",
    "number_of_viewers": None,
    "number_of_reviews": None,
    "site": None,
    "prequisites": None,
    "course_level": None
}

course_2 = {
    "title": "Creative Writing for Beginners",
    "category": "Arts & Humanities",
    "sub_category": "Writing",
    "short_intro": "Explore the fundamentals of storytelling and develop your creative writing skills.",
    "skills": "Storytelling, Grammar, Editing, Creative Thinking",
    "url": "Testing",
    "course_type": "Testing",
    "language": "lang",
    "subtitle_languages": "lang",
    "instructors": "Testing N",
    "rating": None,
    "level": "Advanced",
    "number_of_viewers": None,
    "number_of_reviews": None,
    "site": None,
    "prequisites": None,
    "course_level": None
}

course_not_matching = {
    "title": "Project Management Basics",
    "category": "Business",
    "sub_category": "Management",
    "short_intro": "Learn the fundamentals of project management, including planning, execution, and team coordination.",
    "skills": "Project Planning, Risk Management, Team Leadership, Time Management",
    "url": "Testing",
    "course_type": "Testing",
    "language": "lang",
    "subtitle_languages": "lang",
    "instructors": "Testing N",
    "rating": None,
    "level": "Advanced",
    "number_of_viewers": None,
    "number_of_reviews": None,
    "site": None,
    "prequisites": None,
    "course_level": None
}

competencies = [
    Competency(id=1, name="Creative Expression",
               description="The ability to express thoughts, emotions, and ideas creatively through written forms."),
    Competency(id=2, name="Machine Learning Algorithms",
               description="Understanding and implementation of various machine learning algorithms for predictive modeling and problem-solving.")
]

def test_course_pipeline_first_data():
    pipeline = CoursePipeline(competencies)
    output_data = pipeline._enrich_course(course=course_1)

    assert type(output_data) == Course  # noqa: E721
    assert output_data.matching_competencies == "Machine Learning Algorithms"
    assert output_data.number_of_reviews == 0
    assert output_data.prequisites == ""

def test_course_pipeline_second_data():
    pipeline = CoursePipeline(competencies)
    output_data = pipeline._enrich_course(course=course_2)

    assert type(output_data) == Course  # noqa: E721
    assert output_data.matching_competencies == "Creative Expression"
    assert output_data.number_of_reviews == 0
    assert output_data.prequisites == ""

def test_course_pipeline_unmatch_data():
    pipeline = CoursePipeline(competencies)
    output_data = pipeline._enrich_course(course=course_not_matching)

    assert output_data is None

def test_course_pipeline_full():
    pipeline = CoursePipeline(competencies)
    output_data = pipeline.transform([course_1 ,course_2 ,course_not_matching])
    non_none_data = [x for x in output_data if x is not None]
    assert len(output_data) == 3
    assert len([d for d in output_data if d is None])== 1
    assert [d.matching_competencies for d in non_none_data if d.title=="Introduction to Machine Learning"][0] == "Machine Learning Algorithms"
    assert [d.matching_competencies for d in non_none_data if d.title=="Creative Writing for Beginners"][0] == "Creative Expression"
