import uuid

from flask import jsonify, request
from flask_restplus import Namespace, Resource, reqparse
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from core.model import ClientModel
from core.model import db
from core.service import common_util
from core.service.serialize_obj import serialize

api = Namespace('client')

init_client = reqparse.RequestParser()
init_client.add_argument('name', type=str, required=True)
init_client.add_argument('os', type=str, required=True)
init_client.add_argument('os_username', type=str, required=True)
init_client.add_argument('os_password', type=str, required=True)
init_client.add_argument('model_version', type=str, required=True)
init_client.add_argument('platform_version', type=str, required=True)

register_client = reqparse.RequestParser()
register_client.add_argument('uuid', type=str, required=True)
register_client.add_argument('LAN_IP', type=str, required=True)


@api.route('/init')
class InitClient(Resource):
    """
    初始化一个client信息
    """

    @api.expect(init_client)
    def post(self):
        args = init_client.parse_args()
        client_name = args.name
        # 操作系统、用户名及密码
        os = args.os
        os_username = args.os_username
        os_password = args.os_password
        model_version = args.model_version
        platform_version = args.platform_version

        if ClientModel.query.filter_by(name=client_name).count() > 0:
            msg = 'The name has existed, please entry again!'
            return jsonify({'result': msg, 'status': 400})
        client = ClientModel(name=client_name, uuid=uuid.uuid1(), model_version=model_version,
                             platform_version=platform_version, os=os, os_username=os_username, os_password=os_password)
        db.session.add(client)
        db.session.commit()
        return jsonify({'result': 'Create success', 'status': 200})


@api.route('/register')
class RegisterClient(Resource):
    """
    注册client信息
    """

    @api.expect(register_client)
    def post(self):
        args = register_client.parse_args()
        uuid = args.uuid
        LAN_IP = args.LAN_IP
        public_IP = request.remote_addr
        if not common_util.check_IP(LAN_IP):
            msg = 'The LAN_IP is error, please entry again!'
            return jsonify({'result': msg, 'status': 400})
        try:
            client = ClientModel.query.filter_by(uuid=uuid).one()
        except NoResultFound:
            msg = 'The uuid is error, no such client!'
            return jsonify({'result': msg, 'status': 400})
        except MultipleResultsFound:
            msg = 'Multiple result found of this uuid: {}'.format(uuid)
            return jsonify({'result': msg, 'status': 400})
        # 更新客户端的信息
        client.LAN_IP = LAN_IP
        client.public_IP = public_IP

        # 生成id_rsa
        common_util.generate_id_rsa()

        # TODO 内网穿透并进行ssh_copy_id
        # 下发id_rsa.pub成功后再将更改提交到数据库
        db.session.commit()
        return jsonify({'result': '注册成功!', 'status': 200})


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
