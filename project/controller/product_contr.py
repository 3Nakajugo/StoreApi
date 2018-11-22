from flask import jsonify
from project.db.datab import Database
from project.models import Product


class ProductController:
    def __init__(self):
        self.dbconn = Database()

    def add_product(self, product_name, quantity, unit_price, category):

        product = Product(
            product_name=product_name,
            quantity=quantity,
            unit_price=unit_price,
            category=category
        )

        self.dbconn.post_products(product_name=product.product_name, quantity=product.quantity,
                                  unit_price=product.unit_price, category=product.category)
        return jsonify({"message": "product has been created"})

    # def check_product(self, product_name):
    #     for product in products:
    #         if product["product_name"] == product_name:
    #             return product
    #         return False

    def get_product_list(self):
        return self.dbconn.get_products()

    def get_single_product(self, productid):
        return self.dbconn.get_single_product(productid)

    def delete_product(self, productid):
        self.dbconn.delete_product(productid)
        return jsonify({"message": "product was deleted successfully"})

    # def update_product(self, product_id, product_name, quantity, unit_price, category):
    #     for product in products:
    #         if product.product_id == product_id:
    #             product.update(product_name=product_name,
    #                            quantity=quantity,
    #                            unit_price=unit_price,
    #                            category=category)
    #             return products
