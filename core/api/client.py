from flask import jsonify
from flask_restplus import Namespace, Resource

from core.model import ClientModel
from core.model import db

api = Namespace('client')


@api.route('/')
class Client(Resource):
    def get(self):
        """
        获取所有client的信息
        :return:
        """
        all_client = db.session.query(ClientModel).all()
        return jsonify(all_client)
