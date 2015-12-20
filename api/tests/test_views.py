from nose.tools import eq_
import json

from api import models, server, db

class TestApi:
    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()
        self.txn = db.session.begin_nested()

    def tearDown(self):
        self.txn.rollback()

    def _post_json(self, path, dct):
        json_data = json.dumps(dct)
        json_data_length = len(json_data)
        headers = [('Content-Type', 'application/json'),
                   ('Content-Length', json_data_length)]
        return self.app.post(path, headers=headers, data=json_data)

    def test_hello_world(self):
        rv = self.app.get('/')
        eq_(200, rv.status_code)
        eq_(rv.data, b'Hello World!')

    def test_list(self):
        rv = self.app.get('/todos/')
        eq_(200, rv.status_code)
        body = json.loads(rv.data.decode('utf-8'))
        eq_(0, len(body['items']))

    def test_create(self):
        rv = self._post_json('/todos/', dict(
            title='Title x',
            state='new'
        ))
        eq_(200, rv.status_code)
        body1 = json.loads(rv.data.decode('utf-8'))
        eq_(body1['title'], 'Title x')
        eq_(body1['state'], 'new')

        rv = self.app.get('/todos/%d' % body1['id'])
        eq_(200, rv.status_code)
        body2 = json.loads(rv.data.decode('utf-8'))
        eq_(body1, body2)
