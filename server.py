import os
import threading
import runpy
import asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer

def start_bot():
    # Thread ke andar asyncio event loop create karo
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # bot.py ko aise run karo jaise: python bot.py
    runpy.run_module("bot", run_name="__main__")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is running")

    def log_message(self, format, *args):
        return  # silence logs

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    threading.Thread(target=start_bot, daemon=True).start()

    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()
