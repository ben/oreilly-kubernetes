from api import views, models
import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        views.app.config['TESTING'] = True
        self.app = views.app.test_client()
        models.init_db('api_test')

    def tearDown(self):
        pass
