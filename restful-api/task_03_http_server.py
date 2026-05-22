#!/usr/bin/python3
"""http.server modulu ilə sadə API serverinin qurulması."""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """HTTP GET sorğularını qəbul edən və yönləndirən sinif (handler)."""

    def do_GET(self):
        """Müəyyən edilmiş endpoint-lərə görə GET sorğularını idarə edir."""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server():
    """Serveri 8000 portunda başladan funksiya."""
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server 8000 portunda başladıldı...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dayandırıldı.")
        httpd.server_close()


if __name__ == "__main__":
    run_server()
