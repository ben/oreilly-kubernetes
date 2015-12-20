import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy_utils.functions import database_exists, create_database

# Database connection init
engine = None
session = None

@as_declarative()
class Base():
    id = sa.Column(sa.Integer, primary_key=True)

    @classmethod
    def all(cls):
        return cls.query.all()

    def set_fields(self, dct):
        for k,v in dct.items():
            setattr(self, k, v)

    def save(self):
        session.add(self)
        session.flush()

def init_db(db_name='app_todo'):
    global engine, session
    CONNSTR = 'postgresql+psycopg2://postgres@database/%s' % db_name
    # Ensure the db exists
    if not database_exists(CONNSTR):
        create_database(CONNSTR)
    # Connect
    engine = sa.create_engine(CONNSTR)
    session = scoped_session(sessionmaker(bind=engine))
    Base.query = session.query_property()
