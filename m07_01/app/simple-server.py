from http.server import HTTPServer, BaseHTTPRequestHandler

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Hello world!</h1>
</body>
</html>
"""


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=UTF-8')
        self.end_headers()
        self.wfile.write(html.encode())

    def do_POST(self):
        pass


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    address = 'localhost', 3000
    http = server_class(address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt as err:
        print(err)
    finally:
        http.server_close()


if __name__ == '__main__':
    run()
