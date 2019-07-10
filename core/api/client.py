from flask_restplus import Namespace, Resource

from core.model import UserModel
from core.model import db
from core.service.serialize_obj import serialize

api = Namespace('client')


@api.route('/')
class Client(Resource):
    def get(self):
        """
        获取所有client的信息
        :return:
        """
        all_client = db.session.query(UserModel).all()
        all_client = serialize(all_client)

        return {'result': 'success', 'client_list': all_client}
