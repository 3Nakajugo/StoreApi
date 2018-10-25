from flask import Flask, jsonify, request

app = Flask(__name__)

products = []


@app.route('/api/v1/products', methods=['POST'])
def post_products():
    request_data = request.get_json(force=True)
    new_product = dict()
    if len(products) == 0:
        new_product["product_id"] = 1
    else:
        new_product['product_id'] = products[-1]['product_id']+1
    new_product["name"] = request_data["name"]
    new_product["quantity"] = request_data["quantity"]
    new_product["price"] = request_data["price"]
    if new_product["name"] == "":
        return jsonify({"message": "please input all fields"}), 400
    if new_product["quantity"] == "":
        return jsonify({"message": "please input all fields"}), 400
    if new_product["price"] == "":
        return jsonify({"message": "please input all fields"}), 400
    products.append(new_product)
    return jsonify(new_product), 201
