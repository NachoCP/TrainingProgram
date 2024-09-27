from pymilvus import MilvusClient
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from commons.config import get_environment_variables
from commons.logging import logger

# Runtime Environment Configuration
env = get_environment_variables()

# Generate Database URL

# Create Database Engine
engine = create_engine(env.database_url, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()


def get_milvus_connection():
    if env.ENVIRONMENT == "dev":
        logger.info(f"Connecting Milvus Little and sync in the following file {env.MILVUS_LITTLE}")
        client = MilvusClient(env.MILVUS_LITTLE)
    else:
        logger.info(f"Connecting Milvus Client to the following host http://{env.MILVUS_HOSTNAME}:{env.MILVUS_PORT}")
        client = MilvusClient(uri=f"http://{env.MILVUS_HOSTNAME}:{env.MILVUS_PORT}")
    try:
        yield client
    finally:
        client.close()
