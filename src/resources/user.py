from flask_restful import Resource
from src.token import token_required
class UserRes(Resource):
    @token_required
    def get(self, uuid = None):
        pass
