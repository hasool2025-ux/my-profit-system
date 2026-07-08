import os
import requests
from flask import Flask, request

app = Flask(__name__)

# طباعة تأكيدية عند التشغيل
print("Server is running...")

@app.route('/notify', methods=['POST', 'GET'])
def notify():
    # طباعة البيانات التي تصل للسيرفر في سجلات Railway
    data = request.json
    print(f"Data received: {data}")
    
    if data and 'message' in data:
        message_text = data['message'].get('text', '')
        print(f"Message content: {message_text}")
        
        # رد تلقائي للبوت ليؤكد أنه استلم الرسالة
        token = os.getenv('TELEGRAM_TOKEN')
        chat_id = os.getenv('CHAT_ID')
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {'chat_id': chat_id, 'text': f"تم الاستلام: {message_text}"}
        requests.post(url, data=payload)
        
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
