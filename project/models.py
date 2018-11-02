from flask import jsonify

sales_records = []


class Product:

    def __init__(self, product_name, quantity, unit_price, category):
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

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
