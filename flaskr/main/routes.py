from flask import jsonify, Blueprint, redirect, url_for, request, abort
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


def pagination(request, selection):
    plants_per_page = 5
    # page is part of the get request to specific the pagination page
    page = request.args.get('page', 1, type=int)
    # display 5 element in per page
    start = (page - 1) * plants_per_page
    end = start + plants_per_page
    formatted_plants = [plant.format() for plant in selection[start:end]]
    return formatted_plants


# get all plants
@main.route("/plants")
def get_plants():
    error = False
    try:
        plants = db.session.query(Plant).all()
        total_plant = len(plants)
        formatted_plants = pagination(request, plants)
        if not formatted_plants:
            abort(404)
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
            'Plants': formatted_plants,
            'total_plants': total_plant
        })


@main.route("/plants/<int:plant_id>")
def get_specific_plant(plant_id):
    plant = db.session.query(Plant).get_or_404(plant_id)

    return jsonify({
        'success': True,
        'Plant': plant.format()
    })
