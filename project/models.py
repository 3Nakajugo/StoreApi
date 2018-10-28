from flask import jsonify
products = []
sales_records = []


class Products():

    def __init__(self, name, quantity, price):
        self.product_id = len(products)+1
        self.name = name
        self.quantity = quantity
        self.price = price

    def add_product(self):

        new_product = {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

        products.append(new_product)
        return jsonify(products)

    @staticmethod
    def get_product_list():
        if len(products) > 0:
            return jsonify(products)

    @staticmethod
    def get_single_product(product_id):
        for product in products:
            if product["product_id"] == product_id:
                return jsonify(product)


class SaleRecord():
    def __init__(self, date, items, sale_quantity, prices):
        self.record_id = len(sales_records)+1
        self.date = date
        self.items = items
        self.sale_quantity = sale_quantity
        self.prices = prices

    def add_sale_record(self):
        new_record = {
            "record_id": self.record_id,
            "date": self.date,
            "items": self.items,
            "sale_quantity": self.sale_quantity,
            "prices": self.prices
        }

        sales_records.append(new_record)
        return jsonify(sales_records)

    @staticmethod
    def get_sales_records():
        if len(sales_records) > 0:
            return jsonify(sales_records)

    @staticmethod
    def single_record(record_id):
        for record in sales_records:
            if record["record_id"] == record_id:
                return jsonify(record)
