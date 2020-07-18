from flask import Blueprint

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def handle_404(error):
    return "Not found! once I am initialized, will let you know. Stay awesome!"


@errors.app_errorhandler(405)
def handle_notAllowed(error):
    return "I am not Allowed yet! once they create me, I will let you know. Stay awesome!"
