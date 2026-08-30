from flask import Flask, render_template
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        environment=os.getenv("APP_ENV", "development"),
        version=os.getenv("APP_VERSION", "1.0.0"),
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "devops-dashboard"
    }


@app.route("/api/info")
def info():
    return {
        "application": "DevOps Dashboard",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "development"),
        "hostname": socket.gethostname(),
        "python": os.sys.version
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)