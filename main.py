import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    print(f"Data received: {data}") # هذا سيظهر في الـ Logs
    if data and 'message' in data:
        msg = data['message'].get('text', '')
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      data={'chat_id': CHAT_ID, 'text': f"تم الاستلام: {msg}"})
    return "OK", 200

# ربط تلقائي عند التشغيل
if __name__ == '__main__':
    webhook_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://my-profit-system-production.up.railway.app/notify"
    requests.get(webhook_url)
    app.run(host='0.0.0.0', port=5000)
