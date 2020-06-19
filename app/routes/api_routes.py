from flask import Blueprint, request, jsonify

api = Blueprint("api", __name__)


@api.route("/api/predict", methods=["POST"])
def predict_sub():
    data = request.get_json()
    title = data["title"]
    text = data["description"]

    # TODO
    # Do Stuff
    subreddit = 'r/wallstreetbets'

    return jsonify({"title": title, "text": text, "subreddit": subreddit})
