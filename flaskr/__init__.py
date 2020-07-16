from flask import Flask, jsonify
from config import Config


# main application factory
def create_app(test_config=None):
    # instance_relative_config=True tells the app that configuration files are relative to the instance folder.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Initialize Plugins, Setting plugins as global variables outside of create_app() makes them globally accessible
    # to other parts of our application
    from flaskr.models import db
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing. OVERRIDE the existing configuration
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    with app.app_context():
        # register routes and/or blueprints
        from flaskr import routes

    return app
