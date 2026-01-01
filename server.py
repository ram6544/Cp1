import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import bot   # 👈 YAHAN bot.py import ho rahi hai

PORT = int(os.environ.get("PORT", 10000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is running")

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

def start_bot():
    bot.main()   # 👈 bot.py ka main() run hoga

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()  # 👈 bot background me
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Web server running on port {PORT}")
    server.serve_forever()
