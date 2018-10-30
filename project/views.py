from flask import Flask, jsonify, request

# from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from project.models import Products, SaleRecord, User


from app import app


@app.route('/')
def greet():
    return ('welcome to my store'), 200


@app.route('/api/v1/products', methods=['GET'])
def get_products():

    prod = Products.get_product_list()
    if prod:
        return prod, 200
    return jsonify({"message": "no products to dispaly"}), 400


@app.route('/api/v1/products', methods=['POST'])
def post_products():
    try:

        request_data = request.get_json(force=True)
        name = request_data["name"]
        if name == "":
            return jsonify({"message": "please input product name"}), 400
        quantity = request_data["quantity"]
        if quantity == "":
            return jsonify({"message": "please input product quantity "}), 400
        price = request_data["price"]
        if price == "":
            return jsonify({"message": "please input product price"}), 400
        new_product = Products(name, quantity, price)
        check_product = new_product.check_product(name)
        if not check_product:
            n_product = new_product.add_product()
            return n_product, 201
        return jsonify({"message": "product already exists"})
    except Exception:
        return jsonify({"message": "internal server error"}), 500


@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_single_product(product_id):
    single_product = Products.get_single_product(product_id)
    if single_product:
        return single_product, 200
    return jsonify({"message": "no product with such an Id"}), 404


@app.route('/api/v1/sales', methods=['POST'])
def post_sales_record():
    request_data = request.get_json(force=True)
    try:
        date = request_data["date"]
        if date == "":
            return jsonify({"message": "please input date"}), 400
        items = request_data["items"]
        if items == "":
            return jsonify({"message": "please input item(s) "}), 400
        sale_quantity = request_data["sale_quantity"]
        prices = request_data["prices"]
        if sale_quantity == "" or prices == "":
            return jsonify({"message": "please input quantity or price"}), 400
        new_sales = SaleRecord(date, items, sale_quantity, prices)
        n_sales = new_sales.add_sale_record()
        if n_sales:
            return n_sales, 201
    except Exception:
        return jsonify({"message": "internal server error"}), 500


@app.route('/api/v1/sales', methods=['GET'])
def get_sales_record():
    record = SaleRecord.get_sales_records()
    if record:
        return jsonify(record), 200
    return jsonify({'message': 'no records to display'}), 400


@app.route('/api/v1/sales/<int:record_id>', methods=['GET'])
def get_single_record(record_id):
    s_record = SaleRecord.single_record(record_id)
    if s_record:
        return jsonify({"sale record": s_record}), 200
    return jsonify({"message": "no record with such an Id"}), 404


@app.route('/api/v1/users', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json(force=True)
        user_id = user_data["user_id"]
        username = user_data["username"]
        password = user_data["password"]
        gender = user_data["gender"]

        attendant = User(user_id, username, password, gender)
        user_attendant = attendant.register()
        return user_attendant
    except Exception:
        return jsonify({"message": "please input all feilds"})
