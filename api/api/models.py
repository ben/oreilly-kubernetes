import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import as_declarative

# Database connection init
CONNSTR = 'postgresql+psycopg2://postgres@database/app_api'
engine = sa.create_engine(CONNSTR)
session = scoped_session(sessionmaker(bind=engine))

@as_declarative()
class Base():
    id = sa.Column(sa.Integer, primary_key=True)

    @classmethod
    def query(cls):
        return session.query(cls)

    @classmethod
    def all(cls):
        return cls.query().all()

class Todo(Base):
    __tablename__ = 'todo'
    title = sa.Column(sa.Unicode)
    state = sa.Column(sa.Unicode)