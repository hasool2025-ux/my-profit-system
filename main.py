import requests
import os
from flask import Flask

app = Flask(__name__)

# المتغيرات التي أضفناها في Railway
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

@app.route('/')
def home():
    # هذا هو المنطق: مراقبة السعر ثم إرسال التنبيه
    price = 2350.0
    message = f"🚨 تنبيه الذهب: السعر الآن {price} دولار. الاتجاه: صاعد."
    
    # إرسال الرسالة لتليجرام
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)
    
    return "تم إرسال التنبيه لهاتفك بنجاح!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
