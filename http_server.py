from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<html><body>Ime i Prezime: <b>Zeljko Tadin</b> <br> Datum: <b>5/4/2020</b></body></html>')

PORT = 8000
httpd = HTTPServer(('localhost', PORT), RequestHandler)
print("Serving on port ", PORT)
httpd.serve_forever()