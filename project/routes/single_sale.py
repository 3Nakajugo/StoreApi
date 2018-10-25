from flask import Flask, jsonify, request

app = Flask(__name__)

sales_records = []


@app.route('/api/v1/sales/<int:record_id>', methods=['GET'])
def get_single_record(record_id):
    for record in sales_records:
        if record['record_id'] == record_id:
            return jsonify(record), 200
        return jsonify({'message': "no record with such an id"}), 400
