import unittest

from project.routes.home import app

from project.routes.get_all_products import app

class TestHome(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_message(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
