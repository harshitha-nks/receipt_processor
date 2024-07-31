from flask import Flask, request, jsonify
import uuid
import math

app = Flask(__name__)

receipts = {}

def calculate_points(receipt):
    points = 0

    # Rule 1: One point for every alphanumeric character in the retailer name.
    points += sum(c.isalnum() for c in receipt['retailer'])

    # Rule 2: 50 points if the total is a round dollar amount with no cents.
    total = float(receipt['total'])
    if total.is_integer():
        points += 50

    # Rule 3: 25 points if the total is a multiple of 0.25.
    if total % 0.25 == 0:
        points += 25

    # Rule 4: 5 points for every two items on the receipt.
    points += (len(receipt['items']) // 2) * 5

    # Rule 5: Points based on the description length multiple of 3
    for item in receipt['items']:
        desc_length = len(item['shortDescription'].strip())
        if desc_length % 3 == 0:
            points += math.ceil(float(item['price']) * 0.2)

    # Rule 6: 6 points if the day in the purchase date is odd.
    purchase_day = int(receipt['purchaseDate'].split('-')[2])
    if purchase_day % 2 != 0:
        points += 6

    # Rule 7: 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    purchase_time = receipt['purchaseTime']
    hour, minute = map(int, purchase_time.split(':'))
    if 14 <= hour < 16:
        points += 10

    return points

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    receipt = request.json
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    receipts[receipt_id] = points
    return jsonify({"id": receipt_id})

@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
    if id in receipts:
        return jsonify({"points": receipts[id]})
    return jsonify({"error": "Receipt not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
