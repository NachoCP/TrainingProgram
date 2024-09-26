# Course Data


For this project, I am using [Online Courses Dataset](https://www.kaggle.com/datasets/khaledatef1/online-courses) from Kaggle, which contains extensive information on a variety of courses.

A first analyis has been performed in this [notebook](../data-analysis.ipynb).

The dataset will undergo cleaning, and a sample of 300 courses will be selected to prevent overwhelming the application.

## Workflow

The course data will then be transformed using the following workflow:

1. **Data Cleaning**: The data will first be cleaned by eliminating null values and reformatting where necessary. One of the conditions for inserting data into Milvus is that no data can be null or empty.
2. **Competency Extraction**: A Large Language Model (LLM) will be used to extract competencies from each course. The competencies defined at the company level will be used to match them to the courses. This step enriches the course data by associating company-specific competencies with each course.
3. **Embedding Generation**: An embedding model will be applied to transform the extracted competencies from Step 2 into a list of vectors.
4. **Data Insertion into Milvus**: The processed data, including course information and the embedding vectors, will be inserted into a Milvus collection. This will allow the retrieval of course metadata along with the vectorized embeddings for further use.


![course-workflow](img/course-workflow.png)

## Technical Debt

- **Restricted Course Data Access**: The course data is only accessible through search operations. If you need to use the course data for any other purpose, there is no direct access method available.

- **Limited Data Ingestion Options**: Currently, there is only a bulk ingestion method for courses. There is no option to ingest a single course individually.