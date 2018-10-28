from flask import Flask, jsonify, request

from project.models import Products, SaleRecord

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
    n_product = new_product.add_product()
    if n_product:
        return n_product, 201


@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_single_product(product_id):
    single_product = Products.get_single_product(product_id)
    if single_product:
        return single_product, 200
    return jsonify({"message": "no product with such an Id"}), 400


@app.route('/api/v1/sales', methods=['POST'])
def post_sales_record():
    request_data = request.get_json(force=True)
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


@app.route('/api/v1/sales', methods=['GET'])
def get_sales_record():
    record = SaleRecord.get_sales_records()
    if record:
        return record, 200
    return jsonify({'message': 'no records to display'}), 400


@app.route('/api/v1/sales/<int:record_id>', methods=['GET'])
def get_single_record(record_id):
    s_record = SaleRecord.single_record(record_id)
    if s_record:
        return jsonify({"sale record": s_record}), 200
    return jsonify({"message": "no record with such an Id"}), 400
