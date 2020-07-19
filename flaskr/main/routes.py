from flask import jsonify, Blueprint, redirect, url_for, request, abort
from flask_cors import CORS
from flaskr.models import db, Plant
from .utils import *

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
        formatted_plants, current_page, total_plants = plants_info(request)
    except Exception:
        error = False
    finally:
        db.session.close()

    if error:
        abort(500)
    elif not formatted_plants:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'plants': formatted_plants,
            'current_page': current_page,
            'number_of_plants': total_plants
        })


@main.route("/plants/<int:plant_id>")
def get_specific_plant(plant_id):
    plant = get_plant_or_404(plant_id)

    return jsonify({
        'success': True,
        'Plant': plant.format()
    })


@main.route("/plants", methods=["POST"])
def create_plant():
    error = False

    try:
        body = request.get_json()
        plant = create_new_plant(body)
        plant.insert()
        plant_id = plant.id
        # get plants info
        formatted_plants, current_page_number, total_plants = plants_info(request)
    except Exception:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    if error:
        abort(422)
    else:
        return jsonify({
            "success": True,
            "new_plant_id": plant_id,
            'plants': formatted_plants,
            'current_page_number': current_page_number,
            'number_of_plants': total_plants
        })


@main.route("/plants/<int:plant_id>", methods=["PATCH"])
def update_plant(plant_id):
    plant = get_plant_or_404(plant_id)
    error = False

    try:
        body = request.get_json()
        set_attributes(plant, body)
        plant.update()
        p_name = plant.name
    except Exception:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify({
            'success': True,
            'id': plant_id,
            'name': p_name
        })


@main.route("/plants/<int:plant_id>", methods=["DELETE"])
def delete_plant(plant_id):
    plant = get_plant_or_404(plant_id)
    error = False

    try:
        # delete plant
        plant.delete()
        remaining_plants, current_page, total_plants = plants_info(request)
    except Exception:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify({
            'success': True,
            'deleted_plant_id': plant_id,
            'plants': remaining_plants,
            'current_page': current_page,
            'number_of_plants': total_plants
        })
