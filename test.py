import requests

# URL of the running Flask application
base_url = "http://localhost:5000"

# Data to be sent for processing the receipt
receipt_data = {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
        {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
        {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
        {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
        {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"}
    ],
    "total": "35.35"
}

# Process the receipt
response = requests.post(f"{base_url}/receipts/process", json=receipt_data)
receipt_id = response.json().get("id")
print(f"Receipt ID: {receipt_id}")

# Get points for the processed receipt
points_response = requests.get(f"{base_url}/receipts/{receipt_id}/points")
points = points_response.json().get("points")
print(f"Points: {points}")
