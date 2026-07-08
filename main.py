import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    print(f"DEBUG: Data received: {data}") # سيظهر في الـ Logs
    return "OK", 200

if __name__ == '__main__':
    # ربط وتأكيد الربط في الـ Logs
    webhook_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://my-profit-system-production.up.railway.app/notify"
    response = requests.get(webhook_url)
    print(f"DEBUG: Webhook response: {response.text}") # سيكتب في الـ Logs هل الربط ناجح؟
    
    app.run(host='0.0.0.0', port=5000)
