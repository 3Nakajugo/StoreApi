from flask import jsonify
products = []


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
