from flask import Flask
import threading

app = Flask(__name__)

def start_bot():
    import bot   # 👈 bas import, bot.py khud run ho jayega

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    app.run(host="0.0.0.0", port=10000)
