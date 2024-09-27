# Future Steps




## Architecture

1. **Implement a Base Service/Repository Layer on the Backend**:
    - Base service that encapsulates common CRUD operation for all the services/repositories (respectively).
    - This will reduce code duplication and make it simple.
2. **Robust Error Handling**:
   - Implement a centralized error handling mechanism to track and manage errors such as data insertion failures, validation errors, and duplicate key violations.
   - Better error tracking will help improve system reliability and make it easier to debug issues.
3. **Introduce Caching Mechanism**:
   - Implement a caching mechanism (e.g., Redis or Memcached) to store frequently accessed data, such as user information or course recommendations.
   - Caching will reduce the load on the database, improve response times, and enhance the overall user experience by making frequently accessed data available faster.
4. **Desacople anti-pattern design in the Frontend**:
   - Break down the UI layer into smaller, more focused components to follow the **Single Responsibility Principle (SRP)**. Separate data handling and state management from the UI presentation.
5. **Move Synthetic Data Generation to the Backend**:
   - Shift the synthetic data generation functionality from the frontend to the backend. The backend can generate the data and send it to the frontend through API calls.
6. **Improve Logging system**:
    - The current logging system is a bit terrible and having a better alternative will be great.

## Data Model

1. **Expand Feedback Model**:
   - Enhance the feedback model to support more detailed and dynamic feedback, such as multi-dimensional feedback (e.g., qualitative comments, competency-specific ratings, and 360-degree feedback).
2. **Support for Dynamic Competency Levels**:
    - Make competency levels more dynamic by allowing for multiple levels of granularity (e.g., individual, team, department, and organization-wide).
    - Introducing more granularity will allow managers to better tailor competency requirements based on specific needs across the organization.

## Course Data Ingestion

1. **Store metadata in PostgreSQL**:
   - Store only the relevant information for matching purposes in the vector database (Milvus), while relying on PostgreSQL to store all the metadata. This approach ensures metadata is stored in a single location, reducing redundancy.
   - When a competency is created or updated, the data is updated in PostgreSQL, and only the modified records are synced to the vector database. This prevents the need to completely restore the Milvus database each time a change occurs.
2. **Multi-modal Course Support**:
   - Enable managers to upload new course information not only from platform providers (e.g., Udemy, Coursera) but also in other formats, such as PDFs or videos.
   - This content will be stored in an appropriate format and uploaded to a storage bucket system (e.g., S3, MinIO, Azure Blob Storage) for efficient access and retrieval.

## Recommendation system

1. **Implement a Feedback Course Model**:
    - Introduce a feedback course mechanism where users can provide input about the courses they have done.
    - This will allow the system to learn from user behavior and start applying **Content-Based Filtering** strategies.
    - The [RECOMMENDERS](https://github.com/recommenders-team/recommenders) could be a good start to apply these strategies.
2. **Dynamic Weight Adjustments in Ranking**:
   - Introduce dynamic or personalized weights for the ranking system, allowing users to prioritize factors such as ratings, popularity, or competencies based on their preferences.
3. **Improve Milvus Indexing and Search Techniques**:
   - As the dataset grows, introduce advanced indexing in Milvus (e.g., HNSW, IVF) and explore more efficient search techniques, such as Approximate Nearest Neighbors (ANN).
4. **A/B Testing for Recommendation Effectiveness**:
   - Implement A/B testing to compare different recommendation strategies (e.g., cosine similarity vs. alternative algorithms).
   - Implements [metrics](https://github.com/recommenders-team/recommenders/tree/main/examples/03_evaluate) to evaluate the different recommendation strategies and fine-tune them.