import uuid

from flask import jsonify,request
from flask_restplus import Namespace, Resource, reqparse

from core.model import ClientModel
from core.model import db
from core.service.serialize_obj import serialize

api = Namespace('client')

create_client = reqparse.RequestParser()
create_client.add_argument('name', type=str, required=True)


@api.route('/')
class Client(Resource):
    def get(self):
        """
        获取所有client的信息
        :return:
        """
        all_client = db.session.query(ClientModel).all()
        all_client = serialize(all_client)

        return {'result': 'success', 'client_list': all_client}

    @api.expect(create_client)
    def post(self):
        """
        初始化一个client
        :return:
        """
        args = create_client.parse_args()
        client_name = args.name
        if ClientModel.query.filter_by(name=client_name).count() > 0:
            msg = 'The name has existed, please entry again!'
            return jsonify({'result': msg, 'status': 400})
        client = ClientModel(name=client_name, uuid=uuid.uuid1())
        db.session.add(client)
        db.session.commit()
        return jsonify({'result': 'Create success', 'status': 200})
