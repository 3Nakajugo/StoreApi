products = []


class Products:

    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def add_product(self):
        new_product = {
            "product_id": len(products)+1,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }
        return new_product
        
