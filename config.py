import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRETKEY')
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRESQL') + 'plants'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

# class ProductionConfig(Config):
#     DATABASE_URI = 'mysql://user@localhost/foo'

# class DevelopmentConfig(Config):
#     DATABASE_URI = 'mysql://user@localhost/foo'

# class TestingConfig(Config):
#     TESTING = True
