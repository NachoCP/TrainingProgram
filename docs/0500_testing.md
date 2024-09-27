# Testing

To ensure the robustness and reliability of the services, a comprehensive set of tests has been implemented using pytest. 

## Testing Backend

These tests are designed to validate the behavior of the backend services and repositories, focusing on the interaction with the database systems and the FastAPI framework. 

A variety of pytest fixtures have been created to mock the behavior of the database systems (e.g., SQLLittle, Milvus) and the FastAPI application. These fixtures act as simulated environments for services and repositories, allowing us to test the behavior of the system in a controlled setting without relying on actual databases or API requests.

The test has been split into two:
- **Unit tests**: These tests focus on the repository components, ensuring that the integration with the data layer is correct. SQLLittle is used to mock the relational database, while Milvus Little is used for the vector database, allowing for all necessary operations to be tested.
- **Integration tests**: These tests focus on the FastAPI application, ensuring that all routes and API endpoints function as expected.

There are no tests for the service layer, as its functionality is largely covered by the integration tests. The service layer doesn't handle any complex logic itself; instead, the logic resides in the repository (for data access) and the commons library (for pipelines and recommendations). The services mainly act as intermediaries, calling these two components.

## Testing Frontend

These tests are designed to validate the synthetic data creation process. They cover basic functionalities to ensure that the data is generated correctly by the LLM, as well as standard combinations.

Currently, there are no tests for the service layer. This is considered a "nice to have" for the future to improve test coverage and integration across the entire system.


## Testing LLM

These tests are designed to evaluate the outputs of the LLM models. Since we are using the Instructor library, the outputs are controlled, and we know what type of data will be returned.

However, there are currently no metrics in place to test for issues such as hallucination, ambiguity, or toxic content in the model outputs. Adding these metrics would be a valuable enhancement for the future.

A library that could be considered for this purpose is  [Deepeval](https://docs.confident-ai.com/docs/getting-started), which provides a solid framework for evaluating and testing LLM outputs.

Two model providers have been tested, but the goal of the project is to keep the code agnostic of the specific provider and use whichever one fits best for the purpose. The testing was focused on both accuracy and performance.

- **OpenAI**: This model performs very well in terms of speed, returning data quickly. However, its accuracy and hallucination handling are less reliable. Often, the data returned is not the most relevant, requiring more explicit prompts to generate useful information.

- **Anthropic**: While slightly slower in returning data, this model excels in accuracy. It provides better entity extraction and overall higher-quality data, making it a more suitable option when precision is a priority.