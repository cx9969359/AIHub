from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ClientModel(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    # 初始化时的唯一标识符
    uuid = db.Column(db.String(64), nullable=False)
    # 初始化时的客户端名称，必填
    name = db.Column(db.String(64), unique=True, nullable=False)
    # 操作系统用户名密码
    os_username = db.Column(db.String(64))
    os_password = db.Column(db.String(64))
    # ssh端口
    ssh_port = db.Column(db.Integer, nullable=False)
    # 公网IP
    public_IP = db.Column(db.String(32))
    # 内网IP
    LAN_IP = db.Column(db.String(32))
    # 部署平台操作系统
    os = db.Column(db.String(32))
    # 计算模型版本
    model_version = db.Column(db.String(64))
    # CellPlatform版本
    platform_version = db.Column(db.String(64))
    # 是否已经注册(0否1是)
    register = db.Column(db.Integer, default=0)
    # 注册时间（整数时间戳）
    register_date = db.Column(db.Integer)
    # 运行状态(0否1是)
    status = db.Column(db.Integer, default=0)
