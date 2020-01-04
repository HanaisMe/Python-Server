from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import socketserver

class MyServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>Hi!</h1></body></html>".encode("utf-8"))
        
    def do_POST(self):
        self._set_headers()
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        response = BytesIO()
        response.write(body)
        self.wfile.write(response.getvalue())

def run(server_class = HTTPServer, handler_class = MyServer, port = 8000):
    # server_address = ('', port) # access from anywhere
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

