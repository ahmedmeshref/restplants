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
    # display plants_per_page element in per page
    start = (page - 1) * plants_per_page
    end = start + plants_per_page
    formatted_plants = [plant.format() for plant in selection[start:end]]
    return [formatted_plants, page]


# get all plants
@main.route("/plants")
def get_plants():
    error = False

    try:
        plants = db.session.query(Plant).all()
        total_plant = len(plants)
        formatted_plants, curr_page = pagination(request, plants)
    except:
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
            'Plants': formatted_plants,
            'current_page': curr_page,
            'total_plants': total_plant
        })


@main.route("/plants/<int:plant_id>")
def get_specific_plant(plant_id):
    plant = db.session.query(Plant).get_or_404(plant_id)

    return jsonify({
        'success': True,
        'Plant': plant.format()
    })


def set_attributes(ins, msg):
    if not msg:
        return False
    for key, val in msg.items():
        setattr(ins, key, val or 'not_specified')
    return True


def create_new_plant(body):
    """
    create_new_plant takes in the request body and return a newly created plant
    """
    new_plant = Plant()
    # get data
    attr = {
        'name': body.get('name', 'NA'),
        'scientific_name': body.get('scientific_name', 'NA'),
        'is_poisonous': body.get('is_poisonous', True),
        'primary_color': body.get('primary_color', 'NA')
    }
    set_attributes(new_plant, attr)
    return new_plant


@main.route("/plants", methods=["POST"])
def create_plant():
    error = False

    try:
        body = request.get_json()
        plant = create_new_plant(body)
        plant.insert()
        plant_id = plant.id
        # get all plants
        plants = db.session.query(Plant).all()
        formatted_plants, curr_page = pagination(request, plants)
    except:
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
            "plants": formatted_plants,
            "current_page": curr_page
        })


@main.route("/plants/<int:plant_id>", methods=["PATCH"])
def update_plant(plant_id):
    plant = db.session.query(Plant).get_or_404(plant_id)
    error = False

    try:
        body = request.get_json()
        set_attributes(plant, body)
        plant.update()
        p_name = plant.name
    except:
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
    plant = db.session.query(Plant).get_or_404(plant_id)
    error = False

    try:
        # delete plant
        plant.delete()
        # get remaining plants
        remaining_plants = db.session.query(Plant).all()
        no_plants = len(remaining_plants)
        current_plants, page = pagination(request, remaining_plants)
    except:
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
            'current_plants': current_plants,
            'number_of_plants': no_plants
        })
