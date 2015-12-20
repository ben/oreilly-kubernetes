import sqlalchemy as sa
from .db import Base

class Todo(Base):
    __tablename__ = 'todo'
    title = sa.Column(sa.Unicode)
    state = sa.Column(sa.Unicode)
