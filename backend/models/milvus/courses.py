from pymilvus import CollectionSchema, DataType, FieldSchema


def get_course_schema(embedding_dimension: int) -> CollectionSchema:
    fields = [
        # Campos de metadatos
        FieldSchema(name="title", is_primary=True, dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="url", dtype=DataType.VARCHAR, max_length=512),
        FieldSchema(name="short_intro", dtype=DataType.VARCHAR, max_length=4000),
        FieldSchema(name="category", dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="sub_category", dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="course_type", dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="language", dtype=DataType.VARCHAR, max_length=64),
        FieldSchema(name="subtitle_languages", dtype=DataType.VARCHAR, max_length=512),
        FieldSchema(name="skills", dtype=DataType.VARCHAR, max_length=1024),
        FieldSchema(name="instructors", dtype=DataType.VARCHAR, max_length=512),
        FieldSchema(name="rating", dtype=DataType.FLOAT),
        FieldSchema(name="number_of_viewers", dtype=DataType.FLOAT),
        FieldSchema(name="site", dtype=DataType.VARCHAR, max_length=64),
        FieldSchema(name="level", dtype=DataType.VARCHAR, max_length=64),
        FieldSchema(name="number_of_reviews", dtype=DataType.INT32),
        FieldSchema(name="prequisites", dtype=DataType.VARCHAR, max_length=1024),
        FieldSchema(name="matching_competencies", dtype=DataType.VARCHAR, max_length=512),
        FieldSchema(name="course_level", dtype=DataType.VARCHAR, max_length=64),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=embedding_dimension),
    ]

    return CollectionSchema(fields, description="Course information with embeddings and metadata")
