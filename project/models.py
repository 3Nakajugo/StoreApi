from flask import jsonify

products = []
sales_records = []
users = []


class Product:

    def __init__(self, product_name, quantity, unit_price, category):
        self.product_id = len(products)+1
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.category = category


class SaleRecord:
    def __init__(self, date, items, sale_quantity, total_price):
        self.record_id = len(sales_records)+1
        self.date = date
        self.items = items
        self.sale_quantity = sale_quantity
        self.total_price = total_price


class User:

    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def register(self):
        new_user = {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "role": self.role

            }

        users.append(new_user)
        return users
