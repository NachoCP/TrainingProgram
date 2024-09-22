from commons.interfaces.service import IService
from commons.models.core.competency import Competency


class CompetenciesService(IService):

    def __init__(self,
                 llm_model: str ="gpt-3.5-turbo",
                 llm_provider: str = LLMFactory.openai.value,
                 prompt_path: str = "commons/prompts/template.prompt"
                 ):

        dynamic_competencies = [c["name"] for c in competencies_data]
        CourseModel.set_dynamic_example("matching_competencies", dynamic_competencies)

        self._competencies = '\n'.join([f"- {c['name']}: {c['description']}" for c in competencies_data])

        self._llm_model = llm_model
        self._llm_runner = LLMProviderFactory.get_provider(llm_provider)(CourseModel)
        self._embeddign_runner = EmbeddingProviderFactory.get_provider(embedding_provider)(embedding_model, env.EMBEDDING_DIMENSION)
        self._prompt = PromptTemplate(prompt_path)
        self._milvus_client = MilvusClient(env.MILVUS_LITTLE)
    def create(self, schema: S) -> M:

        pass

    def delete(self, id: K) -> None:

        pass

    def get(self, id: K) -> M:

        pass

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[M]:

        pass

    def update(self, id: K, schema: S) -> M:

        pass
