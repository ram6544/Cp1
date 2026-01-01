import os
import threading
import runpy
from http.server import BaseHTTPRequestHandler, HTTPServer

def start_bot():
    # bot.py ko aise run kare jaise: python bot.py
    runpy.run_module("bot", run_name="__main__")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is running")

    def log_message(self, format, *args):
        return  # logs disable

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    threading.Thread(target=start_bot, daemon=True).start()

    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()
