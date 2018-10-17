from flask import Flask, jsonify, request

app = Flask(__name__)

products = []


@app.route('/')
def greet():
    return ('welcome to my store'), 200


# @app.route('/api/v1/products', methods=['POST'])
# def create_product():
#     request_data = request.get_json(force=True)
#     new_product = dict()
#     if len(products) == 0:
#         new_product["product_id"] = 1
#     else:
#         new_product['product_id'] = products[-1]['product_id']+1
#     new_product["name"] = request_data["name"]
#     new_product["quantity"] = request_data["quantity"]
#     new_product["price"] = request_data["price"]

#     return jsonify(new_product), 201


@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    product = {"product_id": 1,
               "name": "milk",
               "quantity": "10000",
               "price": "2000"
               }
    products.append(product)
    if len(products) > 0:
        return jsonify({'products': products}), 200
    return jsonify({'message': 'no products to display'}), 400


@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_single_product(product_id):
    for product in products:
        if product['product_id'] == product_id:
            return jsonify(product), 200
        return jsonify({'message': 'no product with such an id'}), 404


if __name__ == '__main__':
    app.run(debug=True)
