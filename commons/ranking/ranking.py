from typing import Any, List

from commons.config import get_environment_variables
from commons.constants import (
    MAX_PRIORITY,
    WEIGHTS_SCORING,
)
from commons.embeddings.factory import EmbeddingProviderFactory
from commons.interfaces.ranking import IRanking
from commons.math import cosine_similarity, normalize
from commons.models.recommender.course import CourseModelOutput

env = get_environment_variables()


class CourseRanking(IRanking):

    def __init__(self):
        self._embeddign_runner = EmbeddingProviderFactory.get_provider(
            env.EMBEDDING_PROVIDER_MODEL)()
    def filtering(self,
                  candidates: list[CourseModelOutput],
                  courses_title: list[str]) -> list[dict[str, Any]]:
        # Filter candidates (e.g., remove items the user has already seen)
        return [candidate for candidate in candidates if candidate.title not in courses_title]

    def scoring(self,
                competencies_priority: dict[str, int],
                filtered_data: list[CourseModelOutput]) -> list[dict[ str, Any]]:

        ratings = [course.rating for course in filtered_data]
        viewers = [course.number_of_viewers for course in filtered_data]

        max_rating, min_rating = max(ratings), min(ratings)
        max_viewers, min_viewers = max(viewers), min(viewers)
        max_possible_score = len(competencies_priority) * MAX_PRIORITY

        for course in filtered_data:

            coeff_priority = sum([competencies_priority[competency] for competency in
                                     course.matching_competencies.split(",")
                                     if competency in competencies_priority])

            coeff_priority = normalize(coeff_priority, 0, max_possible_score)

            skills_embedding = self._embeddign_runner.get_embedding(course.skills)
            query_embedding = course.query_embedding
            skills_similarity = cosine_similarity(skills_embedding, query_embedding)

            normalized_rating = normalize(course.rating, min_rating, max_rating)
            normalized_viewers = normalize(course.number_of_viewers, min_viewers, max_viewers)

            final_score = (
                WEIGHTS_SCORING["coeff_priority"] * coeff_priority +
                WEIGHTS_SCORING["matching_competencies"] * course.metric_coefficient +
                WEIGHTS_SCORING["rating"] * normalized_rating +
                WEIGHTS_SCORING["number_of_viewers"] * normalized_viewers +
                WEIGHTS_SCORING["matching_skills"] * skills_similarity
            )
            course.final_score = final_score
        return filtered_data

    def ordering(self, scored_data: List[CourseModelOutput]) -> List[CourseModelOutput]:
        # Order items by their scores
        return sorted(scored_data, key=lambda curso: curso.final_score, reverse=True)
