from flask import current_app as app
from flask import jsonify, Blueprint

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return jsonify({"message": "Hello world"})
