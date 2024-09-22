from typing import Any

from pymilvus import MilvusClient

from commons.config import get_environment_variables
from commons.constants import (
    COURSE_COLLECTION,
    COURSE_OUTPUT_FIELDS,
    DEFAULT_EMBEDDING_MODEL,
    EMBEDDING_COLUMN,
    SEARCH_PARAMS,
    WEIGHTS_SCORING,
)
from commons.embeddings.factory import EmbeddingProviderFactory
from commons.enum import EmbeddingFactory
from commons.interfaces.recommender import IRecommender
from commons.math import cosine_similarity, normalize
from commons.models.recommender.course import CourseModelOutput

env = get_environment_variables()


class CourseRecommender(IRecommender):

    def __init__(self,
                embedding_provider: str = EmbeddingFactory.openai.value,
                embedding_model: str = DEFAULT_EMBEDDING_MODEL):

        self._embeddign_runner = EmbeddingProviderFactory.get_provider(embedding_provider)(embedding_model, env.EMBEDDING_DIMENSION)
        self._milvus_client = MilvusClient(env.MILVUS_LITTLE)

    def candidate_generation(self, input_data: str) -> list[CourseModelOutput]:

        query_embedding = self._embeddign_runner.get_embedding(input_data)
        results = self._milvus_client.search(
            collection_name=COURSE_COLLECTION,
            data=[query_embedding],
            anns_field=EMBEDDING_COLUMN,
            search_params=SEARCH_PARAMS,
            limit=30,
            output_fields=list(COURSE_OUTPUT_FIELDS)
        )
        query_properties = {
            "query_embedding": query_embedding,
            "query_string":  input_data
        }
        output = [CourseModelOutput(**{**{"metric_coefficient": result["distance"]}, **query_properties, **result["entity"]}) for result in results[0]]

        return output

    def filtering(self,
                  candidates: list[CourseModelOutput],
                  courses_title: list[str]) -> list[dict[str, Any]]:
        # Filter candidates (e.g., remove items the user has already seen)
        return [candidate for candidate in candidates if candidate.title not in courses_title]

    def scoring(self, filtered_data: list[CourseModelOutput]) -> list[dict[ str, Any]]:

        ratings = [course.rating for course in filtered_data]
        reviews = [course.number_of_reviews for course in filtered_data]
        viewers = [course.number_of_viewers for course in filtered_data]

        max_rating, min_rating = max(ratings), min(ratings)
        max_reviews, min_reviews = max(reviews), min(reviews)
        max_viewers, min_viewers = max(viewers), min(viewers)

        for course in filtered_data:
            skills_embedding = self._embeddign_runner.get_embedding(course.skills)
            query_embedding = course.query_embedding
            skills_similarity = cosine_similarity(skills_embedding, query_embedding)

            normalized_rating = normalize(course.rating, min_rating, max_rating)
            normalized_reviews = normalize(course.number_of_reviews, min_reviews, max_reviews)
            normalized_viewers = normalize(course.number_of_viewers, min_viewers, max_viewers)

            final_score = (
                WEIGHTS_SCORING["matching_competencies"] * course.metric_coefficient +
                WEIGHTS_SCORING["rating"] * normalized_rating +
                WEIGHTS_SCORING["number_of_reviews"] * normalized_reviews +
                WEIGHTS_SCORING["number_of_viewers"] * normalized_viewers +
                WEIGHTS_SCORING["matching_skills"] * skills_similarity
            )
            course.final_score = final_score
        return filtered_data

    def ordering(self, scored_data: list[CourseModelOutput]) -> list:
        # Order items by their scores
        return sorted(scored_data, key=lambda curso: curso.final_score, reverse=True)
