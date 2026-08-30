from flask import Flask, render_template
import os
import socket
from datetime import datetime

app = Flask(__name__)


def get_app_info():
    return {
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "production"),
        "version": os.getenv("APP_VERSION", "2.0.0"),
        "time": datetime.now().strftime("%d %b %Y, %H:%M:%S"),
    }


@app.route("/")
def home():
    return render_template("index.html", info=get_app_info())


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "devops-dashboard",
        "version": "2.0.0",
    }


@app.route("/api/info")
def api_info():
    return get_app_info()


@app.route("/deploy")
def deploy():
    return {
        "message": "Deployment pipeline is working!",
        "version": "2.0.0",
        "hostname": socket.gethostname(),
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)


@app.route("/version")
def version():
    return {
        "version": "3.0.0",
        "message": "GitHub Actions test deployment"
    }
