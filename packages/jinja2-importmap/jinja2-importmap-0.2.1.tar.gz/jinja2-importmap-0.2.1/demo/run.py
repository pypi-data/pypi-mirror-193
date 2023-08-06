import http.server
import os
import pathlib
import socketserver

import jinja2
import jinja2_importmap

PORT = 8001


def demo():
    path = pathlib.Path(__file__).parent / "node_modules"
    import_map = jinja2_importmap.scan_packages(path)
    return import_map.json(indent=4)


class DemoTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


class DemoHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        with open("index.jinja2") as tpl_file:
            template = jinja2.Template(tpl_file.read())
            page = template.render({
                'import_map': demo(),
            }).encode("utf-8")
            self.wfile.write(page)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with DemoTCPServer(("127.0.0.1", PORT), DemoHandler) as httpd:
        print("Serving demo at port", PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Interrupted, shutting down")
        finally:
            httpd.server_close()
