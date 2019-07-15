import datetime
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
init_client.add_argument('ssh_port', type=int, required=True)
init_client.add_argument('model_version', type=str, required=True)
init_client.add_argument('platform_version', type=str)

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
        ssh_port = args.ssh_port

        if ClientModel.query.filter_by(name=client_name).count() > 0:
            msg = 'The name has existed, please entry again!'
            return jsonify({'result': msg, 'status': 400})
        _uuid = str(uuid.uuid1())
        client = ClientModel(name=client_name, uuid=_uuid, model_version=model_version,
                             platform_version=platform_version, os=os, os_username=os_username, os_password=os_password,
                             ssh_port=ssh_port)
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
        # 校验是否已经注册过
        if client.register == 1:
            msg = 'The client has registered'
            return jsonify({'result': msg, 'status': 400})
        # 更新客户端的信息
        client.public_IP = public_IP
        client.LAN_IP = LAN_IP

        # 生成id_rsa
        common_util.save_id_rsa_to_os()

        # TODO 内网穿透并进行ssh_copy_id
        # 下发id_rsa.pub成功后再将更改提交到数据库
        os_username = ''
        cmd = 'ssh-copy-id -i .ssh/id_rsa.pub {}@{}'.format(os_username, LAN_IP)
        # os.system(cmd)

        # 修改注册状态
        client.register = 1
        client.register_date = datetime.datetime.now()
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


@api.route('/select')
class SelectClient(Resource):
    def get(self):
        """
        按条件筛选用户
        :return:
        """
        args = request.args
        condition = args.get('condition', '')
        if not condition:
            # 查询方法all返回list，不能链式调用，过滤
            all_client = ClientModel.query.all()
            all_client = serialize(all_client)
            return {'result': 'success', 'client_list': all_client}
        if condition == 'init':
            client_set = ClientModel.query.filter_by(register=0).all()
            client_set = serialize(client_set)
            return {'result': 'success', 'client_list': client_set}
        else:
            # condition == 'register'
            client_set = ClientModel.query.filter_by(register=1).all()
            client_set = serialize(client_set)
            return {'result': 'success', 'client_list': client_set}
