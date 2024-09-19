from sqlalchemy.ext.declarative import declarative_base

from backend.config.database import engine

Base = declarative_base()

class EntityMeta(Base):

    __abstract__ = True

    def normalize(self):
        return {
            attr: str(getattr(self, attr))
            for attr in vars(self)
        }

def init_db():
    EntityMeta.metadata.create_all(bind=engine)
