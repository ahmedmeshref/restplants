from flask import jsonify, Blueprint, redirect, url_for
from flask_cors import CORS
from flaskr.models import db, Plant

main = Blueprint('main', __name__)

# enable cors on routes that matches */api/*. They will be accessed from all origins with two methods
CORS(main, resources={r"/api/*": {"origins": "*"}})


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


# get all plants
@main.route("/plants")
def get_plants():
    error = False
    try:
        plants = db.session.query(Plant).all()
        formatted_plants = [plant.format() for plant in plants]
    except:
        error = False
    finally:
        db.session.close()
    if error:
        return jsonify({
            'success': True
        })
    else:
        return jsonify({
            'success': True,
            'Plants': formatted_plants
        })
