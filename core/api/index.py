from flask_restplus import Namespace, Resource

from core.model import UserModel
from core.model import db

api = Namespace('index')


@api.route('/')
class Index(Resource):
    def get(self):
        user = UserModel(name='beautiful')
        db.session.add(user)
        db.session.commit()
        return 'nice'
