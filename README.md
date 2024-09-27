# **Training Program System Overview**

The project aims to build a **training recommendation system** for managers to improve the competencies of their employees based on performance data and predefined competency requirements.

Predefined competency requirements define the number of employees that are required to have the desired level of competency. The competencies requirements can be global (company level) or local (department/team level).
Examples: **Public Speaking** *Expert* 2, **Leadership** *Advanced* 1, etc.

You may assume that the following data is available:

- **Competency descriptions** that vary from company to company
- **Training descriptions** from different providers
- **Employee competency assignments and performance reviews**, including scores, manager's notes, and 360-degree feedback.

## System Design

Given these requirements, the system will focus the following points:

1. **Course Recommendation Based on Competency Requirements**: Given a set of competencies requirements defined, recommend the courses align with those specific needs.
2. **Course Recommendation Based on Feedback**: Analyzing all the available feedback (notes, scores, 360-degree feedback), identifying the competencies reflected in them and recommending courses to improve those competencies.

The combination of these two approaches will be the baseline for the entire system.

The system will rely on LLM to support various functionalities, including:

- Generate structured data from unstructured data.
- Feature transformation.
- Data synthetic generation.

With all of this in mind, the system must be capable of:
1. **Providing a software solution** that follows best practices for recommending algorithms and manipulating data.
2. **Storing data** in an appropriate system/systems with efficient access and retrieval capabilities.
3. **Offering a user-friendly interface** that allows users to easily view results and create an interactive environment for working with the data.
4. **Ensuring comprehensive testing** to validate the system's functionality, performance, and reliability.

## Documentation

Each project document will try to have this information, where applicable:

- **Description**: An overview of the document's purpose and scope.
- **Architecture/Diagram**: Visual representations or explanations of the system's structure.
- **Modules**: A detailed breakdown of the system's modules, including their responsibilities and interactions with other components.
- **Business Logic**: An explanation of the system’s core logic, covering the rules and processes that drive the system’s functionality.

## Index

1. [HOW TO](docs/0100_how_to.md)
   1. [Application](docs/0101_application.md)
2. [Architecture](docs/0200_architecture.md)
   1. [Backend](docs/0201_backend.md)
   2. [Frontend](docs/0202_frontend.md)
   3. [Commons](docs/0203_commons.md)
3. [Data Model](docs/0300_data_model.md)
   1. [Course Data](docs/0301_course_data.md)
4. [Recommendation System](docs/0400_recommendation_system.md)
5. [Testing & Metrics](docs/0500_testing.md)
6. [Future Steps](docs/0600_future_steps.md)