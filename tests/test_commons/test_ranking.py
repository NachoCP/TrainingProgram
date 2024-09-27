from commons.models.recommender.course import CourseModelOutput
from commons.ranking.ranking import CourseRanking


def test_ranking():
    ranking = CourseRanking()

    course_1 = CourseModelOutput(
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
        matching_competencies="AI,Machine Learning",
        course_level="beginner",
        query_embedding=[0.0] * 1536,
        query_string="AI,Machine Learning",
        metric_coefficient=0,
    )

    course_2 = CourseModelOutput(
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
        query_embedding=[0.5] * 1536,
        query_string="AI,Machine Learning",
        metric_coefficient=10,
    )

    courses = [course_1, course_2]

    filtered = ranking.filtering([course_1, course_2], [course_2.title])

    assert len(filtered) == 1
    assert filtered[0] == course_1

    competencies_priorities = {"AI": 4, "Machine Learning": 2}

    scoring_data = ranking.scoring(competencies_priorities, [course_1, course_2])
    assert round(scoring_data[1].final_score, 2) == 3.1
    assert ranking.ordering(scoring_data)[1].title == "Advanced Machine Learning"
