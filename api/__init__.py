from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import Config


def create_app():
    ai_hub = Flask(__name__)
    ai_hub.config.from_object(Config)
    return ai_hub


app = create_app()
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
