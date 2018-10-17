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
        self.assertEqual(response.json, {'message': 'no products to display'})

    def test_get_single_product(self):
        response = self.client.get(
            '/api/v1/products/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_product_that_doesnot_exist(self):
        response = self.client.get(
            '/api/v1/products/3', content_type='application/json')
        self.assertEqual(response.status_code, 404)
