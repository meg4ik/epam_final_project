from flask_restful import Resource
from src.token import token_required

class Profile(Resource):
    @token_required
    def get(self):
        pass
