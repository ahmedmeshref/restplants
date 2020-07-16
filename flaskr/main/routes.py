from flask import jsonify, Blueprint
from flask_cors import CORS

main = Blueprint('main', __name__)

# enable cors on routes that matches */api/*. They will be accessed from all origins with two methods
CORS(main, resources={r"*/api/*": {"origins": "*"}})


# CORS Headers
@main.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response


# CORS is not allowed here since the route doesn't contain /api/, but we can allow it with
# @cross_origin(allow_headers=['Content-Type'])
@main.route("/")
def home():
    return jsonify({"message": "Hello world"})
