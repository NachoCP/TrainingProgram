import os
from typing import Any, Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pymilvus import MilvusClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.config.database import get_db_connection
from backend.models.competency import Competency
from backend.models.competency_level import CompetencyLevel
from backend.models.department import Department
from backend.models.employee import Employee
from backend.models.employee_competency import EmployeeCompetency
from backend.models.employee_department import EmployeeDepartment
from backend.models.feedback import Feedback
from backend.routers.api import router

engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def test_init_db() -> None:
    Competency.metadata.create_all(bind=engine)
    Employee.metadata.create_all(bind=engine)
    Department.metadata.create_all(bind=engine)
    CompetencyLevel.metadata.create_all(bind=engine)
    EmployeeCompetency.metadata.create_all(bind=engine)
    EmployeeDepartment.metadata.create_all(bind=engine)
    Feedback.metadata.create_all(bind=engine)


@pytest.fixture
def test_get_db():
    test_init_db()
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
        engine.dispose()


@pytest.fixture
def test_milvus_client():
    try:
        client = MilvusClient("./testing.db")
        yield client
    finally:
        client.close()
        os.remove("./testing.db")


SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def start_app():
    app = FastAPI()
    app.include_router(router)
    yield app


@pytest.fixture(scope="function")
def db_session() -> Generator[SessionTesting, Any, None]:  # type: ignore
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session  # use the session in tests.
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def milvus_client() -> Generator[MilvusClient, Any, None]:
    client = MilvusClient("testing.db")
    yield client
    client.close()


@pytest.fixture(scope="function")
def client(
    start_app: FastAPI, db_session: SessionTesting, milvus_client: MilvusClient  # type: ignore
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """
    test_init_db()

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    start_app.dependency_overrides[get_db_connection] = _get_test_db
    with TestClient(start_app) as client:
        yield client, db_session, milvus_client
