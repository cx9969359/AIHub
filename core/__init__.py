from json import JSONEncoder

from flask import Flask

from config import Config
from core.api import blueprint
from core.model import *


def create_app():
    ai_hub = Flask(__name__)

    ai_hub.config.from_object(Config)

    ai_hub.register_blueprint(blueprint)

    ai_hub.json_encoder = JSONEncoder

    db.init_app(ai_hub)

    return ai_hub
