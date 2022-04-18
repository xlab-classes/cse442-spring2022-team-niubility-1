# import os

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
db = SQLAlchemy()


login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied.'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    login_manager.init_app(app)
    return app



