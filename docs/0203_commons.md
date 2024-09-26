# Commons

This part of the system is responsible for handling common components shared between the backend and services:

- **Embeddings and LLM**: Contains the logic for generating vector embeddings from strings and interacting with Large Language Models (LLMs) to generate output data.
- **Models**: Includes shared data models used by both the backend and frontend to represent data consistently and ensure data quality.
- **Pipelines**: Manages data transformation pipelines, responsible for feature extraction to be used by other components within the system.
- **Prompts**: Houses text-based prompts and a utility that substitutes necessary variables within these prompts for dynamic usage.
- **Ranking**: Implements the logic for filtering, calculating, and sorting data for the recommendation algorithms.
- **Configs, Constants, and Enums**: Stores all configuration settings, constants, and enumerations that are shared across the system to ensure consistency.


## Technical Decision

### Pydantic

[Pydantic](https://docs.pydantic.dev/latest/) is a data validation library used in Python. All models (apart from those used for database interactions) are loaded using this library to ensure the quality of the data. Additionally, Pydantic plays a key role in generating synthetic data, as the more complete and detailed the Pydantic model is, the more accurate the synthetic data will be.

### Instructor

[Instructor](https://python.useinstructor.com/) is an LLM framework that simplifies extracting structured data, such as JSON, from Large Language Models (LLMs). It is valued for its simplicity, transparency, and user-centric design, and it is built on top of Pydantic. This library is responsible for ensuring that the output from an LLM client (such as Anthropic or OpenAI) is structured according to the desired format.

## Software patterns

- **Factory Pattern**: A factory pattern has been implemented to make Instructor agnostic about the LLM client used. Currently, two LLM clients are supported: Anthropic and OpenAI.