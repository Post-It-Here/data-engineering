from flask import Flask
from .routes.api_routes import api

app = Flask(__name__)

app.register_blueprint(api)

@app.route("/hello")
def hello_world():
    return "Hello, World!"
