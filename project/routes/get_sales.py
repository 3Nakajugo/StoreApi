from flask import Flask, jsonify, request

app = Flask(__name__)

sales_records = []


@app.route('/api/v1/sales', methods=['GET'])
def get_sales_record():
    sale_record = {
        'record_id': 1,
        'date': '10/08/2018',
        'item': ['milk', 'eggs'],
        'quantity': ['2', '3'],
        'price': ['1000', '2000']
    }
    sales_records.append(sale_record)
    if len(sales_records) == 0:
        return jsonify({'message': 'no records to display'})
    return jsonify({"sale_records": sales_records}), 200
