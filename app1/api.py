from flask import Flask, jsonify

app = Flask(__name__)

products = []


@app.route('/')
def greet():
    return ('welcome to my store'), 200


@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    if len(products) > 0:
        return jsonify({'products': products}), 200
    return jsonify({'message': 'no products to display'}), 400


@app.route('/api/v1/products/<int:product_id>')
def get_single_product():
    pass


if __name__ == '__main__':
    app.run(debug=True)
