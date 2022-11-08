from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from pathlib import Path
import mimetypes

BASE_DIR = Path().parent


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        route = urlparse(self.path)
        match route.path:
            case '/':
                self.send_html_file('index.html')
            case '/contact':
                self.send_html_file('contact.html')
            case '/blog':
                self.send_html_file('blog.html')
            case _:
                resource = Path().joinpath(route.path[1:])
                if resource.exists():
                    self.send_static_file(resource)
                else:
                    self.send_html_file('404.html', 404)

    def do_POST(self):
        print(urlparse(self.path))
        data = self.rfile.read(int(self.headers['Content-Length']))
        print(data)
        self.send_html_file('contact.html')

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'text/html; charset=UTF-8')
        self.end_headers()
        with open(filename, encoding='utf-8') as f:
            self.wfile.write(f.read().encode())

    def send_static_file(self, filename, status=200):
        self.send_response(status)
        mt = mimetypes.guess_type(filename)
        if mt[0]:
            self.send_header('Content-Type', mt[0])
        else:
            self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        with open(BASE_DIR / filename, 'rb') as f:
            self.wfile.write(f.read())


def run(server_class=HTTPServer, handler_class=HTTPRequestHandler):
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
