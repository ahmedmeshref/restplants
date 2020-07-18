from flask import Flask
from config import config_by_name
from .models import setup_db


# main application factory
def create_app(config_name='development'):
    # instance_relative_config=True tells the app that configuration files are relative to the instance folder.
    app = Flask(__name__, instance_relative_config=True)
    # load giving configuration name
    app.config.from_object(config_by_name[config_name])

    with app.app_context():
        # setup db for app
        setup_db(app)

        # register routes and/or blueprints
        from .main import routes
        from .errors import error_handler
        app.register_blueprint(routes.main)
        app.register_blueprint(error_handler.errors)

    return app
