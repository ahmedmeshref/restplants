from flaskr.models import db, Plant
from flask import abort

plants_per_page = 5


def pagination(request, selection):
    # page is part of the get request to specific the pagination page
    page = request.args.get('page', 1, type=int)
    # display plants_per_page element in per page
    start = (page - 1) * plants_per_page
    end = start + plants_per_page
    formatted_plants = [plant.format() for plant in selection[start:end]]
    return [formatted_plants, page]


def set_attributes(ins, msg):
    if not msg:
        return abort(400)
    for key, val in msg.items():
        if type(val) == str:
            val.title()
        setattr(ins, key, val or 'not_specified')
    return True


def create_new_plant(body):
    """
    create_new_plant takes in the request body and return a newly created plant
    """
    if not body:
        abort(400)
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


def plants_info(request):
    # get remaining plants
    remaining_plants = db.session.query(Plant).all()
    total_plants = len(remaining_plants)
    formatted_plants, current_page = pagination(request, remaining_plants)
    return [formatted_plants, current_page, total_plants]
