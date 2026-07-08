from flask import Flask, jsonify
import requests

app = Flask(__name__)

# رابط بسيط لجلب سعر الذهب الحالي (محاكاة للسوق)
def get_gold_price():
    # في الاستراتيجية القادمة سنربط هذا ببيانات لحظية دقيقة
    return 2350.00 

@app.route('/')
def analyze_market():
    current_price = get_gold_price()
    # استراتيجية بسيطة: إذا كان السعر فوق 2300 فهو "صاعد"، دونه فهو "هابط"
    trend = "صاعد (Bullish)" if current_price > 2300 else "هابط (Bearish)"
    
    return jsonify({
        "Symbol": "XAUUSD",
        "CurrentPrice": current_price,
        "Trend": trend,
        "SystemStatus": "Active & Analyzing"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
