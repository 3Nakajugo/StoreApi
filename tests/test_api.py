import unittest

from flask import json

from app import app

from project.models import Product


class TestStore(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.sale_record = {
            "date": "12/13/2018",
            "items": ['milk', 'water'],
            "sale_quantity": [2, 4],
            "prices": ['837409237', '78678698']
        }
        self.user = {
            "user_id": 1,
            "username": "edna",
            "password": "edna",
            "role": "store attendant"
        }

    def tearDown(self):
        self.sale_record = None
        self.product = None
        self.app = None

    def test_greet(self):
        response = self.client.get('/api/v1/')
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
        product = Product('water', 50, 1000, 'drinks')
        response = self.client.post(
            '/api/v1/products', content_type='application/json',
            data=json.dumps(dict(name=product.product_name,
                                 quantity=product.quantity,
                                 unit_price=product.unit_price,
                                 category=product.category)))
        self.assertEqual(response.status_code, 201)

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

    def test_sales_record_has_items(self):
        sale_record = {
            "date": "12\30\1998",
            "items": "",
            "sale_quantity": "12",
            "price": "['837409237', '78678698']"
        }
        response = self.client.post(
            '/api/v1/sales', data=json.dumps(sale_record), content_type='application/json')
        self.assertEqual(response.json, {"message": "please input item(s) "})

    def test_sales_record_has_date(self):
        sale_record = {
            "date": "",
            "items": "cups",
            "sale_quantity": "12",
            "price": "['837409237', '78678698']"
        }
        response = self.client.post(
            '/api/v1/sales', data=json.dumps(sale_record), content_type='application/json')
        self.assertEqual(response.json, {"message": "please input date"})

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

    # def test_create_new_user(self):
    #     response = self.client.post(
    #         '/api/v1/users', content_type="application/json", data=json.dumps(self.user))
    #     self.assertEqual(response.status_code, 201)

    # def tests_user_has_all_feilds(self):
        # pass

    # def test_product_already_exists(self):
    #     response = self.client.post(
    #         '/api/v1/products', data=json.dumps(self.product), content_type='application/json')
    #     self.assertEqual(response.json, {"message": "product already exists"})
