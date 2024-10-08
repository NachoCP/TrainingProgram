from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class EntityMeta(Base):

    __abstract__ = True

    def normalize(self):
        return {attr: str(getattr(self, attr)) for attr in vars(self)}
