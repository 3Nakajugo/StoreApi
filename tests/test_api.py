import unittest

from flask import json

from app import app


class TestStore(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.product = {"name": "soap",
                        "quantity": "20",
                        "price": "1500"
                        }

        self.sale_record = {
            "date": "12/13/2018",
            "items": ['milk', 'water'],
            "sale_quantity": [2, 4],
            "prices": ['837409237', '78678698']
        }

    def tearDown(self):
        self.sale_record = None
        self.product = None
        self.app = None

    def test_greet(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_products(self):
        response = self.client.get(
            '/api/v1/products', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_product(self):
        response = self.client.get(
            '/api/v1/products/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        response = self.client.post(
            '/api/v1/products', content_type='application/json', data=json.dumps(self.product))
        self.assertEqual(response.status_code, 201)

    def test_product_content_type(self):
        response = self.client.get(
            '/api/v1/products', content_type='application/json')
        self.assertEqual(json.loads(response.data), [{"name": "soap",
                                                      "price": "1500",
                                                      "product_id": 1,
                                                      "quantity": "20"
                                                      }])

    def test_new_product_has_all_feilds(self):
        product = {"name": "soap",
                   "quantity": "",
                   "price": "1500"
                   }
        response = self.client.post(
            '/api/v1/products', content_type='application/json', data=json.dumps(product))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json, {"message": "please input product quantity "})

    def test_create_sales_record(self):
        response = self.client.post(
            '/api/v1/sales', content_type='application/json', data=json.dumps(self.sale_record))
        self.assertEqual(response.status_code, 201)

    def test_get_all_sales_records(self):
        response = self.client.post(
            '/api/v1/sales', content_type='application/json', data=json.dumps(self.sale_record))
        self.assertEqual(response.status_code, 201)
        response = self.client.get(
            '/api/v1/sales', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_sales_record_hass_all_feilds(self):
        sale_record = {
            "date": "12\30\2018",
            "items": "",
            "sale_quantity": "",
            "price": "['837409237', '78678698']"
        }
        response = self.client.post(
            '/api/v1/sales', data=json.dumps(sale_record), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_single_record(self):
        response = self.client.get(
            '/api/v1/sales/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_record_that_doesnot_exist(self):
        response = self.client.get(
            '/api/v1/sales/4', content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_get_product_that_doesnot_exist(self):
        response = self.client.get(
            '/api/v1/products/30', content_type='application/json')
        self.assertEqual(response.status_code, 404)
