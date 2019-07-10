from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


class ClientModel(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    # 部署平台操作系统
    os = db.Column(db.String(32), default='')
    # 计算模型版本
    model_version = db.Column(db.String(64), default='')
    # CellPlatform版本
    platform_version = db.Column(db.String(64), default='')
    # 上线状态(0否1是)
    status = db.Column(db.Integer)
