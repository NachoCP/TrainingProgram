from backend.repositories.milvus.course_repository import CourseRepository
from commons.models.core.course import Course


def test_success_course_repo(test_milvus_client) -> None:
    repository = CourseRepository(test_milvus_client)

    course_1 = Course(
        title="Introduction to AI",
        url="https://example.com/ai-course",
        short_intro="A beginner-friendly introduction to artificial intelligence.",
        category="Technology",
        sub_category="Artificial Intelligence",
        course_type="video",
        language="English",
        subtitle_languages="Spanish, French",
        skills="AI basics, Machine Learning",
        instructors="Andrew Ng",
        rating=4.8,
        number_of_viewers=10000,
        site="Coursera",
        level="beginner",
        number_of_reviews=2000,
        prequisites="None",
        matching_competencies="AI, Machine Learning",
        course_level="beginner",
        embedding=[0.0] * 1536,
    )

    course_2 = Course(
        title="Advanced Machine Learning",
        url="https://example.com/advanced-ml-course",
        short_intro="A deep dive into advanced machine learning techniques.",
        category="Technology",
        sub_category="Machine Learning",
        course_type="text",
        language="English",
        subtitle_languages="German, Italian",
        skills="Deep Learning, Reinforcement Learning",
        instructors="Ian Goodfellow",
        rating=4.9,
        number_of_viewers=5000,
        site="Udacity",
        level="advanced",
        number_of_reviews=1500,
        prequisites="Introduction to Machine Learning",
        matching_competencies="Deep Learning, AI",
        course_level="advanced",
        embedding=[0.5] * 1536,
    )

    courses = repository.bulk([course_1, course_2])

    assert len(courses) == 2

    query_embedding = [0.5] * 1536
    query_string = "Hello, It's me"

    course_output = repository.search(query_embedding, query_string)

    assert course_output[0].title == "Advanced Machine Learning"
    assert course_output[0].language == "English"
    assert course_output[0].query_string == query_string
    assert course_output[0].query_embedding == query_embedding
