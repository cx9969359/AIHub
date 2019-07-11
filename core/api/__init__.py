from flask import Blueprint
from flask_restplus import Api

from core.api.client import api as client_api

blueprint = Blueprint('aihub', __name__, url_prefix='/AIHub')

api = Api(blueprint)
api.add_namespace(client_api)
