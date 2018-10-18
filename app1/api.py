from flask import Flask, jsonify, request

app = Flask(__name__)

products = []
sales_records = []


@app.route('/')
def greet():
    return ('welcome to my store'), 200


@app.route('/api/v1/products', methods=['GET', 'POST'])
def get_or_post_products():
    if request.method == 'POST':
        request_data = request.get_json(force=True)
        new_product = dict()
        if len(products) == 0:
            new_product["product_id"] = 1
        else:
            new_product['product_id'] = products[-1]['product_id']+1
        new_product["name"] = request_data["name"]
        new_product["quantity"] = request_data["quantity"]
        new_product["price"] = request_data["price"]
        if (new_product["name"] == "" or new_product["quantity"] == "" or new_product["price"] == ""):
            return jsonify({"message": "please input all fields"}), 400
        products.append(new_product)
        return jsonify(new_product), 201
    else:
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
    try:
        int(product_id)
    except:
        return jsonify({'message': 'product_id should be an integer'}), 400
    for product in products:
        if product['product_id'] == product_id:
            return jsonify(product), 200
        return jsonify({'message': 'no product with such an id'}), 404


@app.route('/api/v1/sales', methods=['POST', 'GET'])
def get_post_sales_record():
    if request.method == 'POST':
        request_data = request.get_json(force=True)
        new_record = dict()
        if len(sales_records) == 0:
            new_record["record_id"] = 1
        else:
            new_record['record_id'] = sales_records[-1]['record_id']+1
        new_record["date"] = request_data["date"]
        new_record["item"] = request_data["item"]
        new_record["quantity"] = request_data["quantity"]
        new_record["price"] = request_data["price"]
        if (new_record["item"] == "" or new_record["quantity"] == "" or new_record["price"] == ""):
            return jsonify({"message": "please input all fields"}), 400
        sales_records.append(new_record)
        return jsonify(new_record), 201
    else:
        return jsonify({"sale_records": sales_records}), 200


@app.route('/api/v1/sales/<int:record_id>', methods=['GET'])
def get_single_entry(record_id):
    for record in sales_records:
        if record['record_id'] == record_id:
            return jsonify(record), 200
        return jsonify({'message': "no record with such an id"}), 400
