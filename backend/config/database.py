from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from commons.config import get_environment_variables

# Runtime Environment Configuration
env = get_environment_variables()

# Generate Database URL

# Create Database Engine
engine = create_engine(
    env.database_url, future=True
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()
