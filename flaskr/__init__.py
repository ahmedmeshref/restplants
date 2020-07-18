from flask import Flask
from config import Config
from .models import setup_db


# main application factory
def create_app(test_config=None):
    # instance_relative_config=True tells the app that configuration files are relative to the instance folder.
    app = Flask(__name__, instance_relative_config=True)
    # default configuration
    app.config.from_object(Config)

    if test_config is None:
        # load the instance config, if it exists, when not testing. OVERRIDE the existing configuration
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_object(test_config)

    with app.app_context():
        # setup db for app
        setup_db(app)

        # register routes and/or blueprints
        from .main import routes
        from .errors import error_handler
        app.register_blueprint(routes.main)
        app.register_blueprint(error_handler.errors)

    return app
