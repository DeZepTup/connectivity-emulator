from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)


@app.route("/generate_204")
def generate_204():
    response = Response(status=204)
    response.headers["Content-Length"] = "0"
    response.headers["Cross-Origin-Resource-Policy"] = "cross-origin"
    response.headers["Date"] = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
