from flask import Flask, render_template
import os
import socket
from datetime import datetime

app = Flask(__name__)


def get_app_info():
    return {
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "time": datetime.now().strftime("%d %b %Y, %H:%M:%S")
    }


@app.route("/")
def home():
    return render_template("index.html", info=get_app_info())


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "devops-dashboard"
    }


@app.route("/api/info")
def api_info():
    return get_app_info()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
