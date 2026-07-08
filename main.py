import os
import re
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text, 'parse_mode': 'Markdown'}
    requests.post(url, data=payload)

@app.route('/notify', methods=['POST'])
def notify():
    # هذا المسار يستقبل الرسالة المحولة (Forwarded)
    data = request.json
    message_text = data.get('message', {}).get('text', '')

    # منطق استخراج البيانات (سعر الدخول والهدف)
    # يبحث عن أي أرقام تتبع كلمات مثل buy أو entry
    if "buy" in message_text.lower():
        formatted_msg = f"🟢 *توصية شراء جديدة*\n\n{message_text}"
        send_to_telegram(formatted_msg)
    
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
