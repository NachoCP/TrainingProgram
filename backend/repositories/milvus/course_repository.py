from typing import List

from pymilvus import MilvusClient

from backend.models.milvus.courses import get_course_schema
from commons.config import get_environment_variables
from commons.constants import COURSE_COLLECTION
from commons.models.core.course import Course

env = get_environment_variables()

class CourseRepository():
    def __init__(self, client: MilvusClient) -> None:
        self.client = client
        if not self.client.has_collection(COURSE_COLLECTION):
            self.client.create_collection(
                collection_name=COURSE_COLLECTION,
                schema=get_course_schema(env.EMBEDDING_DIMENSION)
            )

    def bulk(self, instances: List[Course]) -> List[Course]:

        data = [instance.model_dump() for instance in instances]

        self.client.insert(
            collection_name=COURSE_COLLECTION,
            data=data
        )

        index_params = self.client.prepare_index_params()
        index_params.add_index(
            field_name="embedding",
            metric_type="IP",
            index_type="FLAT",
            index_name="vector_index",
            params={ "nlist": 128 }
        )

        self.client.create_index(
            collection_name=COURSE_COLLECTION,
            index_params=index_params
        )

        return instances
