from flask import Flask, jsonify

app = Flask(__name__)

products = []


@app.route('/api/v1/products/<>', methods=['GET'])
def get_products():
    product = {"product_id": 1,
               "name": "milk",
               "quantity": "10000",
               "price": "2000"
               }
    products.append(product)
    if len(products) > 0:
        return jsonify({'products': products}), 200
    return jsonify({'message': 'no products to display'}), 400
