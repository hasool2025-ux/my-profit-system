from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "System is Online and Running 24/7"

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    while True:
        print("الخوارزمية تعمل الآن وتراقب البيانات...")
        time.sleep(60)
