from api import views, models, server
import unittest

models.init_db('app_test')

class AppTestCase(unittest.TestCase):
    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()
        self.txn = models.session.begin_nested()

    def tearDown(self):
        self.txn.rollback()
