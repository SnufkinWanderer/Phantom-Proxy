import http.server, socketserver, time, random
from urllib.parse import urlparse, parse_qs
from ..utils import stealth_delay, log_request
from .payloads import inject_payloads, is_interesting

class StealthProxy(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        stealth_delay()
        log_request(f"[GET] {self.path}")
        self.path = inject_payloads(self.path, "xss")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"<html><body><h1>Intercepted</h1><p>{self.path}</p></body></html>".encode())

    def do_POST(self):
        stealth_delay()
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len).decode()
        log_request(f"[POST] {self.path} - {body[:100]}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST intercepted by PhantomProxy.")

def run_proxy(port=8080):
    with socketserver.TCPServer(("0.0.0.0", port), StealthProxy) as httpd:
        print(f"[+] Proxy running on port {port}")
        httpd.serve_forever()