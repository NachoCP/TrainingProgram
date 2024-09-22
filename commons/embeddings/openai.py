from dotenv import load_dotenv
from openai import OpenAI

from commons.interfaces.embedding import IEmbedding

load_dotenv()

class OpenAIEmbeddingProvider(IEmbedding):
    def __init__(self,
                 model: str = "text-embedding-3-small",
                 embedding_dimension: int = 1536):
        self._client = OpenAI()
        self._model = model
        self._embedding_dimension = embedding_dimension

    def get_embedding(self, text: str) -> list:
        text = text.replace("\n", " ")
        response = self._client.embeddings.create(input=[text],
                                                 model=self._model,
                                                 dimensions=self._embedding_dimension)
        return response.data[0].embedding
