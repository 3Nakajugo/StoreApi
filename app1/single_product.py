from flask import Flask, jsonify

app = Flask(__name__)

products = []


@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_single_product(product_id):
    try:
        int(product_id)
    except:
        return jsonify({'message': 'product_id should be an integer'}), 400
    for product in products:
        if product['product_id'] == product_id:
            return jsonify(product), 200
        return jsonify({'message': 'no product with such an id'}), 404
