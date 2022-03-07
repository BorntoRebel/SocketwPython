from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import socketserver
import time

HOST = "localhost"
PORT = 3000


class ServerHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Conetent-type", "text/html")
        self.end_headers()

        self.wfile.write(
            bytes("<html><body><h1>KEN IS POGI!</h1</body></html", "utf-8")
        )

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime((time.time)))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))


Server = ThreadingHTTPServer((HOST, PORT), ServerHTTP)
print("server think ken is also pogi")
Server.serve_forever()
Server.server_close()
print("stop")
