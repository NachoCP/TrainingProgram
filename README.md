# **Training Program System Overview**

The project aims to build a **training recommendation system** for managers to improve the competencies of their employees based on performance data and predefined competency requirements. The system will use **LLMs (Large Language Models)** to suggest relevant training courses, **PostgreSQL** for relational data storage, and **Milvus** for storing course embeddings.

## **System Architecture**

Below is an outline of the components, their descriptions, and how they interact:

---

### **1. PostgreSQL Database**
Stores all company-specific and employee-specific data:

- **Employee Data**: Stores details of employees, competencies, and teams.
- **Competency Data**: Defines competency levels (e.g., beginner, advanced, expert) and stores feedback (e.g., manager reviews, 360 feedback).
- **Manager and Team Data**: Information about managers, teams, and the relationships between employees and managers.

> **Assumptions**:  
> - Each company may have different competency definitions.  
> - Employee competency levels and feedback are stored per employee.  
> - Competencies are tagged based on performance feedback from multiple sources (e.g., manager notes, reviews).

---

### **2. Milvus Vector Database**
Stores training course embeddings and supports vector search for recommendations.

- **Training Course Embeddings**: LLM-based embeddings of courses stored in Milvus, representing the topics and competencies each course covers.
- **Course-Competency Association**: An LLM identifies the competencies relevant to each course and maps them to competency vectors.

> **Assumptions**:  
> - Each training provider’s description is converted into an embedding that encodes its competency coverage.  
> - The system uses embeddings to associate courses with the required competencies.

---

### **3. Training Recommendation Engine**
Provides managers with course recommendations based on employee performance, competency requirements, and feedback.

- **Competency Gap Analysis**: Uses a LLM to analyze performance data and identify missing competencies that need improvement for each employee.
- **Course Ranking & Recommendation**: Retrieves top K courses based on competency requirements and ranks them according to relevance and quality.

> **Assumptions**:  
> - The LLM is fine-tuned to understand competency gaps based on performance feedback and competency levels.  
> - The ranking system could use techniques like **Neural Collaborative Filtering** or **Learning to Rank** to recommend the best courses.

---

### **4. Backend (FastAPI)**
Handles API requests from the frontend and manages communication with PostgreSQL, Milvus, and the recommendation engine.

- **Competency Management**: APIs for managers to define and update competencies for their teams.
- **Feedback Integration**: APIs for submitting and retrieving feedback from multiple sources.
- **Training Recommendations**: API that triggers the recommendation engine, fetches the recommended courses, and returns the list to the frontend.

> **Assumptions**:  
> - The backend adheres to **SOLID** principles, making it extensible and maintainable.
> - **Dependency Injection** is used to decouple different services such as PostgreSQL, Milvus, and the recommendation engine.
> - Proper API versioning to ensure backward compatibility as features grow.

---

### **5. Frontend (Streamlit)**
A dashboard for managers to interact with the system, define team competencies, view training recommendations, and submit feedback.

- **Competency Overview**: Allows managers to define competency requirements and view current levels.
- **Training Course Recommendations**: Displays the top K recommended courses for each employee and enables course assignment.
- **Feedback Submission**: A form for managers to submit performance feedback.

> **Assumptions**:  
> - The frontend is kept simple using Streamlit, with forms and dashboards to facilitate easy interaction.
> - Role-based access control (e.g., different views for managers and employees).
> - Templated and reusable UI components follow **DRY** principles.

---

## **ML/DL/LLM Models**

- **LLM for Course Embeddings**:  
  A model like **OpenAI GPT-4** or **Hugging Face BERT** fine-tuned on domain-specific training data to convert training course descriptions into embeddings. The model learns the relationship between course content and competencies, mapping courses to the required skill sets.

- **Competency Gap Analysis**:  
  An LLM fine-tuned on employee feedback data (e.g., performance reviews, 360 feedback). The LLM can summarize the feedback and determine the competencies the employee needs to improve on.

- **Recommendation Ranking Model**:  
  A **Neural Collaborative Filtering** model or **Learning to Rank (LTR)** approach can be used to rank courses based on how well they match the competency gap for each employee. It can combine similarity scores with manager preferences and course success rates.

---

## **Software Practices**

### **SOLID Principles**
- **Single Responsibility Principle (SRP)**:  
  Each component (e.g., recommendation engine, data layer, ML model) will have one responsibility, ensuring they are easy to maintain and extend.
  
- **Open-Closed Principle (OCP)**:  
  The system will allow extension of features (e.g., adding new ML models) without modifying the existing code.

- **Liskov Substitution Principle (LSP)**:  
  Abstract base classes will be used for defining interfaces to allow future model swapping without breaking the system.

- **Interface Segregation Principle (ISP)**:  
  Define narrow, specific interfaces for each component (e.g., different APIs for feedback management, course recommendations, and competency tracking).

- **Dependency Inversion Principle (DIP)**:  
  Use dependency injection to ensure that components are not tightly coupled to low-level modules (e.g., DB connections, APIs).

---

### **Test-Driven Development (TDD)**
- Unit tests for all individual components (database models, API endpoints).
- Integration tests for end-to-end functionality (e.g., from feedback submission to course recommendation).
- Mocking external services (e.g., Milvus and LLM models) in unit tests.

---

### **KISS (Keep It Simple, Stupid)**
- Keep the system modular and straightforward, focusing on the MVP requirements. Avoid over-engineering by adding unnecessary complexity.

---

## **Technical Debt & Future Improvements**

### **Handling Scalability**:  
The MVP may not handle massive amounts of training data efficiently. Later, course embeddings and employee competencies could be cached or precomputed to speed up recommendations.

### **Model Performance**:  
The current system assumes an off-the-shelf LLM and embedding-based search for course recommendations. In the future, we can improve with domain-specific fine-tuning or use more advanced recommendation algorithms (e.g., graph-based methods).

### **Feedback Integration**:  
Initial feedback analysis could be simplified, but expanding it to include more robust NLP models for sentiment analysis or competency tagging could improve future versions.

### **Real-Time Adaptation**:  
Future iterations can improve the system to make real-time course recommendations by continually tracking and updating employee competency levels.

### **Data Governance**:  
As the system deals with sensitive employee data, future enhancements could introduce encryption for sensitive fields, audit logging, and compliance with privacy laws (e.g., GDPR).

---

## **Conclusion**

This MVP design follows good software practices (SOLID, TDD, and KISS) and sets a strong foundation for a training recommendation system. It provides a clear architecture with modular components that can be scaled and improved in future versions. Future improvements focus on enhancing scalability, model accuracy, and data handling, ensuring the system grows as company needs evolve.
