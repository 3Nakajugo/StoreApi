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
            "item": ['milk', 'water'],
            "quantity": [2, 4],
            "price": ['837409237', '78678698']
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

    # def test_empty_product_list(self):
    #     response = self.client.get(
    #     '/api/v1/products', content_type='application/json')


    # def test_new_product_has_all_feilds(self):
    #     product = {"name": "soap",
    #                "quantity": "",
    #                "price": "1500"
    #                }
    #     response = self.client.post(
    #         '/api/v1/products', content_type='application/json', data=json.dumps(product))
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(
    #         response.json, {"message": "please input name ,quantity, price"})

    # def test_create_sales_record(self):

    #     response = self.client.post(
    #         '/api/v1/sales', content_type='application/json', data=json.dumps(self.sale_record))
    #     self.assertEqual(response.status_code, 201)

    # def test_sales_record_hass_all_feilds(self):
    #     sale_record = {
    #         "item": "",
    #         "quantity": "",
    #         "price": "['837409237', '78678698']"
    #     }
    #     response = self.client.post(
    #         '/api/v1/sales', data=json.dumps(sale_record), content_type='application/json')
    #     self.assertEqual(response.status_code, 400)

    # def test_get_all_sales_records(self):
    #     response = self.client.post(
    #         '/api/v1/sales', content_type='application/json', data=json.dumps(self.sale_record))
    #     self.assertEqual(response.status_code, 201)
    #     response = self.client.get(
    #         '/api/v1/sales', content_type='application/json')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_single_record_or_product(self):
    #     response = self.client.get(
    #         '/api/v1/sales/1', content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     response = self.client.get(
    #         '/api/v1/products/1', content_type='application/json')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_single_record_or_product_that_doesnot_exist(self):
    #     response = self.client.get(
    #         '/api/v1/sales/30', content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
    #     response = self.client.get(
    #         '/api/v1/products/3', content_type='application/json')
    #     self.assertEqual(response.status_code, 404)
