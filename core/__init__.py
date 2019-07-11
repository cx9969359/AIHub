from flask import Flask

from config import Config
from core.api import blueprint
from core.model import *
from flask_bootstrap import Bootstrap


def create_app():
    ai_hub = Flask(__name__)

    ai_hub.config.from_object(Config)

    ai_hub.register_blueprint(blueprint)

    Bootstrap(ai_hub)

    db.init_app(ai_hub)

    return ai_hub
