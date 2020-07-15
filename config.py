import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRETKEY')
    DEBUG = True
    ENV = 'D'
    TESTING = False
    DATABASE_URI = os.environ.get('POSTGRESQL') + "plants"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

# class ProductionConfig(Config):
#     DATABASE_URI = 'mysql://user@localhost/foo'


# class TestingConfig(Config):
#     TESTING = True
