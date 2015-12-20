from nose.tools import eq_
import json

from api import models, server, db

class TestApi:
    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()
        self.txn = db.session.begin_nested()
        db.session.add(models.Todo(id=1,
                                   state='open',
                                   title='Say Hello'))

    def tearDown(self):
        self.txn.rollback()

    def test_hello_world(self):
        rv = self.app.get('/')
        eq_(200, rv.status_code)
        eq_(rv.data, b'Hello World!')

    def test_list(self):
        rv = self.app.get('/todos/')
        eq_(200, rv.status_code)
        body = json.loads(rv.data.decode('utf-8'))
        eq_(1, len(body['items']))
