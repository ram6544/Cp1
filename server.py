import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

def start_bot():
    import bot   # bot.py import hone se run ho jayega

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is running")

    def log_message(self, format, *args):
        return  # disable default logs

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    threading.Thread(target=start_bot, daemon=True).start()
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()
