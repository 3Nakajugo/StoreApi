import unittest

from flask import json

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
        # self.assertEqual(len(products), 0)

    def test_get_single_product(self):
        response = self.client.get(
            '/api/v1/products/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_product_that_doesnot_exist(self):
        response = self.client.get(
            '/api/v1/products/3', content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_create_product(self):
        product = {"name": "soap",
                   "quantity": "20",
                   "price": "1500"
                   }
        response = self.client.post(
            '/api/v1/products', content_type='application/json', data=json.dumps(product))
        self.assertEqual(response.status_code, 201)

    def test_new_product_has_all_feilds(self):
        product = {"name": "",
                   "quantity": "",
                   "price": ""
                   }
        response = self.client.post(
            '/api/v1/products', content_type='application/json', data=json.dumps(product))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message": "please input all fields"})

    def test_create_sales_record(self):
        sale_record = {
            "date": "12/13/2018",
            "item": "['milk','water']",
            "quantity": "[2,4]",
            "price": "['837409237', '78678698']"
        }
        response = self.client.post(
            '/api/v1/sales', content_type='application/json', data=json.dumps(sale_record))
        self.assertEqual(response.status_code, 201)

    def test_sales_record_hass_all_feilds(self):
        sale_record = {
            "date": "12/13/2018",
            "item": "",
            "quantity": "[2,4]",
            "price": "['837409237', '78678698']"
        }
        response = self.client.post(
            '/api/v1/sales', content_type='application/json', data=json.dumps(sale_record))
        self.assertEqual(response.status_code, 400)

    def test_get_all_sales_records(self):
        sale_record = {
            "date": "12/13/2018",
            "item": "['milk','water']",
            "quantity": "[2,4]",
            "price": "['837409237', '78678698']"
        }
        response = self.client.post(
            '/api/v1/sales', content_type='application/json', data=json.dumps(sale_record))
        self.assertEqual(response.status_code, 201)
        response = self.client.get(
            '/api/v1/sales', content_type='application/json')
        self.assertEqual(response.status_code, 200)
