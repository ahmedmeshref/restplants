from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)


# note: errors and success responses needs to be consistence, format JSON
@errors.app_errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'Resource not found!'
    }), 404


@errors.app_errorhandler(405)
def not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': "Not allowed!"
    }), 405


@errors.app_errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': "Unprocessable request!"
    }), 422


@errors.app_errorhandler(500)
def server_damage(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': "Internal server error!"
    }), 500
