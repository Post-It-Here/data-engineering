from flask import Flask
from .routes.home_routes import home_routes

app = Flask(__name__)

app.register_blueprint(home_routes)

@app.route("/hello")
def hello_world():
    return "Hello, World!"
