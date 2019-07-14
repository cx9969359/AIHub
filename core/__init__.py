from flask import Flask
from flask_cors import CORS

from config import Config
from core.api import blueprint
from core.model import *


def create_app():
    ai_hub = Flask(__name__)

    ai_hub.config.from_object(Config)

    ai_hub.register_blueprint(blueprint)

    db.init_app(ai_hub)
    CORS(ai_hub, resources=r'/*')

    return ai_hub
