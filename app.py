from flask import Flask, make_response
from datetime import datetime, timezone

app = Flask(__name__)


@app.route("/generate_204")
def generate_204():
    response = make_response("", 204)
    response.headers["Content-Length"] = "0"
    response.headers["Cross-Origin-Resource-Policy"] = "cross-origin"
    response.headers["Date"] = datetime.now(timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    )
    response.headers.pop("Server", None)
    response.headers.pop("Content-Type", None)
    return response


@app.route("/connecttest.txt")
def connecttest():
    response = make_response("Microsoft Connect Test", 200)
    response.headers["Content-Type"] = "text/plain"
    response.headers["Content-Length"] = str(len(response.data))
    response.headers["Date"] = datetime.now(timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    )
    response.headers.pop("Server", None)
    return response


@app.route("/")
@app.route("/captive.apple.com")
def captive_apple():
    response = make_response(
        "<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>", 200
    )
    response.headers["Content-Type"] = "text/html"
    response.headers["Content-Length"] = str(len(response.data))
    response.headers["Date"] = datetime.now(timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    )
    response.headers.pop("Server", None)
    return response


@app.route("/generate_204_chromeos")
def generate_204_chrome():
    response = make_response("", 204)
    response.headers["Content-Length"] = "0"
    response.headers["Date"] = datetime.now(timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    )
    response.headers.pop("Server", None)
    response.headers.pop("Content-Type", None)
    return response


@app.route("/generate_204_ubuntu")
def connectivity_check_ubuntu():
    response = make_response("Network OK", 200)
    response.headers["Content-Type"] = "text/plain"
    response.headers["Content-Length"] = str(len(response.data))
    response.headers["Date"] = datetime.now(timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    )
    response.headers.pop("Server", None)
    return response


class StripServerHeaderMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        def custom_start_response(status, headers, exc_info=None):
            headers = [
                (name, value) for name, value in headers if name.lower() != "server"
            ]
            headers = [
                (name, value)
                for name, value in headers
                if not (name.lower() == "date" and "Date" in dict(headers))
            ]
            return start_response(status, headers, exc_info)

        return self.app(environ, custom_start_response)


if __name__ == "__main__":
    app.wsgi_app = StripServerHeaderMiddleware(app.wsgi_app)
    app.run(host="0.0.0.0", port=80)
