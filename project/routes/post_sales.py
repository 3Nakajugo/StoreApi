from flask import Flask, jsonify, request

app = Flask(__name__)

sales_records = []


@app.route('/api/v1/sales', methods=['POST'])
def post_sales_record():
    request_data = request.get_json(force=True)
    new_record = dict()
    if sales_records == []:
        new_record["record_id"] = 1
    else:
        new_record['record_id'] = sales_records[-1]['record_id']+1
    new_record["date"] = request_data["date"]
    new_record["item"] = request_data["item"]
    new_record["quantity"] = request_data["quantity"]
    new_record["price"] = request_data["price"]
    if new_record["item"] == "":
        return jsonify({"message": "please input all fields"}), 400
    if new_record["price"] == "":
        return jsonify({"message": "please input all fields"}), 400
    if new_record["quantity"] == "":
        return jsonify({"message": "please input all fields"}), 400
    sales_records.append(new_record)
    return jsonify(new_record), 201
