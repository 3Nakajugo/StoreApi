from project.models import products


class ProductController:

    def add_product(self, product_id,  product_name, quantity, unit_price, category):

        product = dict(
            product_id=product_id,
            product_name=product_name,
            quantity=quantity,
            unit_price=unit_price,
            category=category
        )

        products.append(product)
        return products

    def check_product(self, product_name):
        for product in products:
            if product["product_name"] == product_name:
                return product
            return False

    def get_product_list(self):
        if len(products) > 0:
            return products

    def get_single_product(self, product_id):
        for product in products:
            if product["product_id"] == product_id:
                return product

    def delete_product(self, product_id):
        for product in products:
            if product["product_id"] == product_id:
                products.remove(product)
                return products
