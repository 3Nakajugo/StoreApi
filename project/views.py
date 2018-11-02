from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity
from project.models import Product, SaleRecord, User, sales_records
from project.validator import Validator
from controller.product_contr import ProductController
from controller.sales_contr import SalesController
from controller.user_contr import UserController
from app import app
from project.db.datab import Database


valid = Validator()
product_controller = ProductController()
sales_controller = SalesController()
database_query = Database()
user_controller = UserController()


@app.route('/api/v2/')
def greet():
    return ('welcome to my store'), 200


@app.route('/api/v2/products', methods=['POST'])
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
    product_obj = Product(product_name,
                          quantity, unit_price, category)
    add_product = product_controller.add_product(
        product_name=product_obj.product_name, quantity=product_obj.quantity, unit_price=product_obj.unit_price, category=product_obj.category)
    if add_product:
        return jsonify({"message": "product has been created"}), 201
    return jsonify({"message": "product not created"})


@app.route('/api/v2/products', methods=['GET'])
def get_products():
    prod = product_controller.get_product_list()
    if prod:
        return jsonify({"message": prod}), 200
    return jsonify({"message": "no products to display"})


@app.route('/api/v2/products/<int:productid>', methods=['GET'])
def get_single_product(productid):
    validate_id = valid.validate_id(productid)
    if validate_id:
        return jsonify({"message": "product id must be integer"}), 400
    single_product = product_controller.get_single_product(productid=productid)
    if single_product:
        return jsonify(single_product), 200
    return jsonify({"message": "no product with such an Id"}), 404


@app.route('/api/v2/products/<int:productid>', methods=['DELETE'])
def delete_single_product(productid):
    delete_product = product_controller.delete_product(productid)
    if delete_product:
        return jsonify({"message": "product was deleted successfully"})
    return jsonify({"message": "no product with such an Id"}), 404


# @app.route('/api/v1/products/<int:product_id>', methods=['PUT'])
# def update_single_product(product_id):
#     request_data = request.get_json()
#     product_name = request_data["product_name"]
#     quantity = request_data["quantity"]
#     unit_price = request_data["unit_price"]
#     category = request_data["category"]
#     updated_product = product_controller.update_product(product_id,
#                                                         product_name, quantity, unit_price, category)
#     if updated_product:
#         return jsonify(products), 201
#     return jsonify({"message": "no product with such an Id"}), 404


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


@app.route('/api/v2/users/signup', methods=['POST'])
def create_user():
    user_data = request.get_json()
    username = user_data["username"]
    password = user_data["password"]
    role = user_data["role"]
    validate_user = valid.validate_user(username, password, role)
    if validate_user:
        return jsonify({"message": "user is not valid"})
    attendant = User(username, password, role)
    user_attendant = user_controller.register_user(
        username=attendant.username, password=attendant.password, role=attendant.role)
    if user_attendant:
        return jsonify({"message": "user was created"}), 201
    return jsonify({"message": "user has not been created"}), 400


@app.route('/api/v2/users/login', methods=['POST'])
def login_user():
    try:
        user_data = request.get_json()
        username = user_data["username"]
        password = user_data["password"]
        login = database_query.login(username, password)
        if login:
            token = {}
            access_token = create_access_token(identity=username)
            token["token"] = access_token
            return jsonify(token), 200
        return jsonify({"message": "failed to login"})
    except:
        return jsonify({"message": "token was not created"})
