from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, unquote_plus
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import mimetypes
import json

BASE_DIR = Path().parent
env_jinja2 = Environment(loader=FileSystemLoader('templates'))


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        route = urlparse(self.path)
        match route.path:
            case '/':
                self.send_html_file('index.html')
            case '/contact':
                self.send_html_file('contact.html')
            case '/blog':
                self.render_template('blog.html')
            case _:
                resource = Path().joinpath(route.path[1:])
                if resource.exists():
                    self.send_static_file(resource)
                else:
                    self.send_html_file('404.html', 404)

    def do_POST(self):
        print(urlparse(self.path))
        data = self.rfile.read(int(self.headers['Content-Length']))
        self.save_post_data_to_json(data)
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

    def save_post_data_to_json(self, data):
        parse_data = unquote_plus(data.decode(), encoding='utf-8')
        result = dict([el.split('=') for el in parse_data.split('&')])
        with open('./storage/post_data.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)

    def render_template(self, filename):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=UTF-8')
        self.end_headers()
        with open('./storage/fake_db.json', 'r', encoding='utf-8') as f:
            blogs = json.load(f)
        template = env_jinja2.get_template(filename)
        html = template.render(title='Blog page!!!', blogs=blogs)
        self.wfile.write(html.encode())


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

# https://replit.com/@Krabaton/web-app#main.py
