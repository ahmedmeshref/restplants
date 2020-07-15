from flask import current_app as app
from flask import jsonify


@app.route("/")
def home():
    return jsonify({"message": "Hello world"})
