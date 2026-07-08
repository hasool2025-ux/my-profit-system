import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    if data and 'message' in data:
        message_text = data['message'].get('text', '')
        
        # هنا يتم فحص الرسالة إذا كانت تحتوي على كلمة "buy"
        if "buy" in message_text.lower():
            response_text = f"✅ وجدتها! هذه توصية شراء:\n\n{message_text}"
        else:
            response_text = "الرسالة لا تحتوي على 'Buy'."
            
        # إرسال الرد
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      data={'chat_id': CHAT_ID, 'text': response_text})
                      
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
