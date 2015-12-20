import sqlalchemy as sa
from .db import Base

class Todo(Base):
    __tablename__ = 'todo'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Unicode)
    state = sa.Column(sa.Unicode)
