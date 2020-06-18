from flask import Blueprint, request, jsonify

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/predict", methods=["POST"])
def predict_sub():
    data = request.get_json()
    title = data["title"]
    text = data["text"]

    # TODO
    # Do Stuff
    subreddit = 'r/wallstreetbets'

    return jsonify({"title": title, "text": text, "subreddit": subreddit})
