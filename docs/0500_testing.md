# Testing

To ensure the robustness and reliability of the services, a comprehensive set of tests has been implemented using pytest. 

## Testing Backend

These tests are designed to validate the behavior of the backend services and repositories, focusing on the interaction with the database systems and the FastAPI framework. 

A variety of pytest fixtures have been created to mock the behavior of the database systems (e.g., SQLLittle, Milvus) and the FastAPI application. These fixtures act as simulated environments for services and repositories, allowing us to test the behavior of the system in a controlled setting without relying on actual databases or API requests.

The test has been splitted into two:
- **Unit tests**: These tests focus on the repository components, ensuring that the integration with the data layer is correct. SQLLittle is used to mock the relational database, while Milvus Little is used for the vector database, allowing for all necessary operations to be tested.
- **Integration tests**: These tests focus on the FastAPI application, ensuring that all routes and API endpoints function as expected.

There are no tests for the service layer, as its functionality is largely covered by the integration tests. The service layer doesn't handle any complex logic itself; instead, the logic resides in the repository (for data access) and the commons library (for pipelines and recommendations). The services mainly act as intermediaries, calling these two components.

## Testing Frontend


