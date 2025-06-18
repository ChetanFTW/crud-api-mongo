from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    from .routes import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    return app
