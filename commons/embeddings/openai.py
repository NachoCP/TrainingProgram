from openai import OpenAI

from commons.config import get_environment_variables
from commons.interfaces.embedding import IEmbedding

env = get_environment_variables()

class OpenAIEmbeddingProvider(IEmbedding):
    def __init__(self):
        self._client = OpenAI(api_key=env.EMBEDDING_KEY)
        self._model = env.EMBEDDING_MODEL
        self._embedding_dimension = env.EMBEDDING_DIMENSION

    def get_embedding(self, text: str) -> list:
        text = text.replace("\n", " ")
        response = self._client.embeddings.create(input=[text],
                                                 model=self._model,
                                                 dimensions=self._embedding_dimension)
        return response.data[0].embedding
