-- Optional: Enum definitions
CREATE TYPE required_level_enum AS ENUM ('basic', 'intermediate', 'advanced', 'expert');
CREATE TYPE role_enum AS ENUM ('Manager', 'Worker');

-- Table: competency
CREATE TABLE competency (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

-- Table: department
CREATE TABLE department (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table: employee
CREATE TABLE employee (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    expiration_date DATE,
    effective_date DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Table: employee_competency
CREATE TABLE employee_competency (
    id INTEGER PRIMARY KEY,
    employee_id INTEGER NOT NULL,
    competency_id INTEGER NOT NULL,
    current_level VARCHAR(255) NOT NULL,
    expiration_date DATE,
    effective_date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (employee_id) REFERENCES employee(id),
    FOREIGN KEY (competency_id) REFERENCES competency(id)
);

-- Table: department_employee
CREATE TABLE employee_department (
    id INTEGER PRIMARY KEY,
    employee_id INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    expiration_date DATE,
    effective_date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (employee_id) REFERENCES employee(id),
    FOREIGN KEY (department_id) REFERENCES department(id)
);

-- Table: competency_level
CREATE TABLE competency_level (
    id INTEGER PRIMARY KEY,
    competency_id INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    required_level required_level_enum NOT NULL,  -- Using PostgreSQL enum
    num_workers INTEGER NOT NULL,
    FOREIGN KEY (competency_id) REFERENCES competency(id),
    FOREIGN KEY (department_id) REFERENCES department(id)
);