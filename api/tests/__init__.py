from api import views, models, server
import unittest

models.init_db('app_test')


class AppTestCase(unittest.TestCase):
    def setUp(self):
        print('SETUP')
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()

    def tearDown(self):
        print('TEARDOWN')
        pass
