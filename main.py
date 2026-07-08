from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def get_market_data():
    # استخدام رابط بيانات السوق
    url = "https://public.api.exness.com/v1/market-data/XAUUSD"
    try:
        # هنا سنقوم بجلب السعر (مثال توضيحي)
        return jsonify({"symbol": "XAUUSD", "price": "2350.00", "status": "Live Data"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
