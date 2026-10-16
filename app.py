
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def get_response():
    return {
        "message": "Wrong Message!",
        "version": "2.0.0",
        "status": "running"
    }


class WebHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path not in ["/", "/health"]:
            self.send_error(404)
            return

        result = get_response()
        output = json.dumps(result).encode("utf-8")

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "application/json"
        )
        self.send_header(
            "Content-Length",
            str(len(output))
        )
        self.end_headers()
        self.wfile.write(output)


if __name__ == "__main__":
    server = HTTPServer(
        ("0.0.0.0", 8000),
        WebHandler
    )

    print("Web server running on port 8000", flush=True)
    server.serve_forever()
