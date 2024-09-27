# How To

The idea of this document is to provide a guide through the different steps of the application.

## Prerequisites: configure .env file

Mandatory to have installed docker and docker-compose.

<details>
  <summary>Configure environment variabls</summary>

You should create a *.env* file in the root directory of the project to load all the environment variables required. There is [template file](../.env_template) with all the necessary information.

- **API_VERSION**: version of the API.
- **APP_NAME**: name of the app.
- **ENVIRONMENT**: environment where the system is located. The idea is that if you change from dev to compose, it will switch from Milvus little to a Milvus standalone instance.
- **BACKEND_HOSTNAME**: hostname of the backend container, this hostname should be the same as that in the [docker-compose](../docker-compose.yml).
- **BACKEND_PORT**: port of the backend container, this port should be the same as that in the [docker-compose](../docker-compose.yml).
- **FRONTEND_PORT**:port of the frontend container, this port should be the same that in the [docker-compose](../docker-compose.yml).
- **DATABASE_HOSTNAME**: hostname of the database container, this hostname should be the same as that in the [docker-compose](../docker-compose.yml).
- **DATABASE_PORT**: port of the database container, this port should be the same as that in the [docker-compose](../docker-compose.yml).
- **DATABASE_DIALECT**: the dialect of the database container, to connect this system.
- **DATABASE_NAME**: name of the database where all the operations are going to be done.
- **DATABASE_USERNAME**: name of the user for the database service.
- **DATABASE_PASSWORD**: name of the password used.
- **EMBEDDING_PROVIDER_MODEL**: embedding provider to use its embedding models, right now it is only available openai.
- **EMBEDDING_MODEL**: embedding model allowed by the provider to be used. For OpenAI check this [list](https://platform.openai.com/docs/guides/embeddings/embedding-models).
- **EMBEDDING_DIMENSION**: embedding dimension that should return the embedding model. Check the model's limitations to see the maximum number allowed.
- **EMBEDDING_KEY**: token key of the provider to be used by the application. Check this [link](https://platform.openai.com/api-keys) to generate the OpenAI key.
- **LLM_PROVIDER_MODEL**: LLM provider to use its llm models, right now it is only available openai and anthropic.
- **LLM_MODEL**: llm model allowed by the provider to be used. Check the list from [OpenAI](https://platform.openai.com/docs/models/o1) and [Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) to select the model.
- **LLM_KEY**: token key of the provider to be used by the application.
- **MILVIS_LITTLE**: name of the Milvus little file used for storing all the vectorial database.
- **MILVUS_HOSTNAME**: hostname of the Milvus container, this hostname should be the same as that in the [docker-compose](../docker-compose.yml).
- **MILVUS_PORT**: port of the Milvus container, this port should be the same as that in the [docker-compose](../docker-compose.yml).

>> NOTE: It is very important to **configure the correct parameters** for the EMBEDDING and LLM attributes. Check the provider's proper names to set up all the ENV variables.
>> NOTE: It is important to rename this file from **.env_template** to **.env**
</details>

## Commands

Once the prerequisites have been done, there are two main commands for launching everythin

It will launch everything using docker-compose to set up all the services. Wait a few seconds before accessing the app.

```bash
make run
```

It will tear down all the containers plus deleting any temporal data generated during the application.

```bash
make stop
```

Once everything is ready, please go to [Application Documentation](0101_application.md) to check the documentation.

The application will be ready in http://localhost:8501/