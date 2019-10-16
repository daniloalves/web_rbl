#!/usr/bin/env python
"""
Very simple HTTP server in python (Updated for Python 3.6)
Usage:
    ./http_server.py -h
    ./http_server.py -l localhost -p 8000
Send a GET request:
    curl http://localhost:8000/ask?ip=1.2.3.4
"""
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import query_ip

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message, api=False):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = ''
        if api:
            content = f"{message}"
        else:
            content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers()
        msg = "hi!"
        if "?" in self.path:
            action = self.path.split("/")[1]
            action = action.split("?")[0]       
            ip = ''
            for key,value in dict(urllib.parse.parse_qsl(self.path.split("?")[1], True)).items():
                if key == 'ip':
                    ip = value
            if action == 'ask':
                msg = query_ip.main(ip)

        self.wfile.write(self._html(msg,api=True))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        #content_length = int(self.headers['Content-Length'])
        #post_data = self.rfile.read(content_length)
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(self._html("POST!"))

def run(server_class=HTTPServer, handler_class=S, addr="0.0.0.0", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="0.0.0.0",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)