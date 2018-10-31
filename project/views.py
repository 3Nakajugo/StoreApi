from flask import Flask, jsonify, request
from project.models import Product, SaleRecord, products, sales_records
from project.validator import Validator
from controller.product_contr import ProductController
from controller.sales_contr import SalesController
from app import app

valid = Validator()
product_controller = ProductController()
sales_controller = SalesController()


@app.route('/api/v1/')
def greet():
    return ('welcome to my store'), 200


@app.route('/api/v1/products', methods=['POST'])
def post_products():
    request_data = request.get_json()
    product_name = request_data["product_name"]
    quantity = request_data["quantity"]
    unit_price = request_data["unit_price"]
    category = request_data["category"]
    validate_product = valid.valid_add_product(
        product_name, quantity, unit_price, category)
    if validate_product:
        return jsonify({"message": "product is invalid"}), 400
    product_obj = Product(product_name, quantity, unit_price, category)
    add_product = product_controller.add_product(
        product_id=product_obj.product_id, product_name=product_obj.product_name, quantity=product_obj.quantity, unit_price=product_obj.unit_price, category=product_obj.category)
    check_product = product_controller.check_product(product_name)
    if isinstance(check_product, Product):
        return jsonify({"message": "product already exists"}), 400
    return jsonify(add_product), 201


@app.route('/api/v1/products', methods=['GET'])
def get_products():
    prod = product_controller.get_product_list()
    if prod:
        return jsonify({"products": prod}), 200
    return jsonify({"message": "no products to dispaly"}), 400


@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_single_product(product_id):
    validate_id = valid.validate_id(product_id)
    if validate_id:
        return jsonify({"message": "product id must be integer"}), 400
    single_product = product_controller.get_single_product(product_id)
    if single_product:
        return jsonify(single_product), 200
    print("reached here")
    return jsonify({"message": "no product with such an Id"}), 404


@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_single_product(product_id):
    delete_product = product_controller.delete_product(product_id)
    if delete_product:
        return jsonify(products), 200
    return jsonify({"message": "no product with such an Id"}), 404


@app.route('/api/v1/sales', methods=['POST'])
def post_sales_record():
    request_data = request.get_json()
    date = request_data["date"]
    items = request_data["items"]
    sale_quantity = request_data["sale_quantity"]
    total_price = request_data["total_price"]
    validate_sale = valid.validate_new_record(
        date, items, sale_quantity, total_price)
    if validate_sale:
        return jsonify({"message": "sale_record is invalid"})
    sale = SaleRecord(date, items, sale_quantity, total_price)
    new_sales = sales_controller.add_sale_record(record_id=sale.record_id,
                                                 date=sale.date,
                                                 items=sale.items,
                                                 sale_quantity=sale.sale_quantity,
                                                 total_price=sale.total_price)
    if new_sales:
        return jsonify(sales_records), 201


@app.route('/api/v1/sales', methods=['GET'])
def get_sales_record():
    record = sales_controller.get_sales_records()
    if record:
        return jsonify({"SALES": sales_records}), 200
    return jsonify({'message': 'no records to display'}), 400


@app.route('/api/v1/sales/<int:record_id>', methods=['GET'])
def get_single_record(record_id):
    s_record = sales_controller.single_record(record_id)
    if s_record:
        return jsonify({"sale record": s_record}), 200
    return jsonify({"message": "no record with such an Id"}), 404


@app.route('/api/v1/sales/<int:record_id>', methods=['DELETE'])
def delete_sales_record(record_id):
    delete_sales = sales_controller.delete_single_product(record_id)
    if delete_sales:
        return jsonify(sales_records)


# @app.route('/api/v1/users', methods=['POST'])
# def create_user():
#     try:
#         user_data = request.get_json(force=True)
#         user_id = user_data["user_id"]
#         if user_id == "":
#             return jsonify({'message': 'please input user_id'}), 400
#         username = user_data["username"]
#         if username == "":
#             return jsonify({'message': 'please input username'}), 400
#         password = user_data["password"]
#         if password == "":
#             return jsonify({'message': 'please input password'}), 400
#         role = user_data["role"]
#         if role == "":
#             return jsonify({'message': 'please input user role'}), 400
#         attendant = User(user_id, username, password, role)
#         user_attendant = attendant.register()
#         return jsonify(user_attendant), 201
#     except Exception:
#         return jsonify({"message": "please input all feilds"})
