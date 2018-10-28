from flask import Flask, jsonify, request

from project.models import Products

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
    if not quantity or quantity == "":
        return jsonify({"message": "please input product quantity "}), 400
    price = request_data["price"]
    if not price or price == "":
        return jsonify({"message": "please input product price"}), 400
    new_product = Products(name, quantity, price)
    n_product = new_product.add_product()
    if n_product:
        return n_product, 201
    return jsonify({"message": "product not created"}), 400


@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_single_product(product_id):
    single_product = Products.get_single_product(product_id)
    if single_product:
        return single_product, 200
    return jsonify({"message": "no product with such an Id"}), 400


# @app.route('/api/v1/sales', methods=['POST'])
# def post_sales_record():
#     request_data = request.get_json(force=True)
#     new_record = dict()
#     if sales_records == []:
#         new_record["record_id"] = 1
#     else:
#         new_record['record_id'] = sales_records[-1]['record_id']+1
#     new_record["date"] = request_data["date"]
#     new_record["item"] = request_data["item"]
#     new_record["quantity"] = request_data["quantity"]
#     new_record["price"] = request_data["price"]
#     if (new_record["item"] == ""or new_record["price"] == "" or new_record["quantity"] == "" or new_record["date"] == ""):
#         return jsonify({"message": "please input all fields"}), 400
#     sales_records.append(new_record)
#     return jsonify(new_record), 201


# @app.route('/api/v1/sales/<int:record_id>', methods=['GET'])
# def get_single_record(record_id):
#     for record in sales_records:
#         if record['record_id'] == record_id:
#             return jsonify(record), 200
#         return jsonify({'message': "no record with such an id"}), 400


# @app.route('/api/v1/sales', methods=['GET'])
# def get_sales_record():
#     sale_record = {
#         'record_id': 1,
#         'date': '10/08/2018',
#         'item': ['milk', 'eggs'],
#         'quantity': ['2', '3'],
#         'price': ['1000', '2000']
#     }
#     sales_records.append(sale_record)
#     if len(sales_records) == 0:
#         return jsonify({'message': 'no records to display'})
#     return jsonify({"sale_records": sales_records}), 200
