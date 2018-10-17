import unittest

from app1.api import app


class TestStore(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_greet(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_products(self):
        response = self.client.get(
            '/api/v1/products', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_empty_list(self):

        response = self.client.get(
            '/api/v1/products', content_type='application/json')
        self.assertEqual(response.status_code, 400)
