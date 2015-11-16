from nose.tools import eq_
import json

from . import AppTestCase
from api import models

class TestApi(AppTestCase):
    def setUp(self):
        super().setUp()
        # Fixture data
        models.session.add(models.Todo(id=1,
                                       state='open',
                                       title='Say Hello'))

    def test_hello_world(self):
        rv = self.app.get('/')
        eq_(200, rv.status_code)
        eq_(rv.data, b'Hello World!')

    def test_list(self):
        rv = self.app.get('/todos/')
        eq_(200, rv.status_code)
        body = json.loads(rv.data.decode('utf-8'))
        eq_(1, len(body['items']))
