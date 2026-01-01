import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# Simple HTTP handler (Render ke liye)
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is running")

# Web server function
def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Web server running on port {port}")
    server.serve_forever()

# Web server ko background thread me chalao
threading.Thread(target=run_server, daemon=True).start()

# Telegram bot start (bot.py run hoga)
import bot
