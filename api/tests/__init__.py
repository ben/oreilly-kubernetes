from api import views, db, server
import unittest

import sys
db.init_db('todo_test')

db.Base.metadata.create_all(bind=db.engine)
server.app.debug = True
