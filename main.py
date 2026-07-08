import requests
import os
from flask import Flask

app = Flask(__name__)

# جلب البيانات من إعدادات Railway
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

@app.route('/notify')
def send_alert():
    price = 2350.00 # هذا الرقم سيتحدث لاحقاً ببيانات حقيقية
    message = f"تنبيه الذهب: السعر الآن {price} دولار. السوق في حالة نشطة."
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    response = requests.get(url)
    return "تم إرسال التنبيه لهاتفك!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
