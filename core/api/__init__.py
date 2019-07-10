from flask import Blueprint
from flask_restplus import Api

from core.api.index import api as index_api

blueprint = Blueprint('aihub', __name__, url_prefix='/AIHub')

api = Api(blueprint)
api.add_namespace(index_api)
