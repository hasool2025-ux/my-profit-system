from flask import Flask, jsonify
import requests

app = Flask(__name__)

# هذا الرابط يمثل "قناة الاتصال" مع بيانات السوق (سعر الذهب)
# ملاحظة: في النسخة الاحترافية سنضع هنا الـ API الخاص بـ Exness
MARKET_DATA_URL = "https://api.exness.com/v1/market-data/XAUUSD"

@app.route('/')
def check_market():
    # هنا المحرك يقوم "بجس نبض" السوق
    try:
        # نقوم بقراءة السعر الحالي للذهب
        response = {"status": "connected", "symbol": "XAUUSD", "price": "2350.50"} 
        # ملاحظة: هذا نموذج تجريبي، سنربطه بـ API Key الخاص بك لاحقاً
        return jsonify(response)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
