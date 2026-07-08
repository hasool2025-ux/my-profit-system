import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# هذا المسار هو الذي سيستقبل الرسائل من تليجرام
@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    if data and 'message' in data:
        message_text = data['message'].get('text', '')
        # هنا سنرسل الرسالة التي استلمناها إلى تليجرام مرة أخرى
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {'chat_id': CHAT_ID, 'text': f"وصلتني رسالة: {message_text}"}
        requests.post(url, data=payload)
    return "OK", 200
import requests

# هذا الكود سيحاول ربط البوت تلقائياً عند تشغيل السيرفر
def setup_webhook():
    token = os.getenv('TELEGRAM_TOKEN')
    url = f"https://my-profit-system-production.up.railway.app/notify"
    webhook_url = f"https://api.telegram.org/bot{token}/setWebhook?url={url}"
    try:
        requests.get(webhook_url)
    except:
        pass

setup_webhook() # استدعاء الدالة عند التشغيل
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
