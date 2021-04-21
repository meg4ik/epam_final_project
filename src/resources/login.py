from flask_restful import Resource
from flask import render_template, make_response, request
from ..database.models import User

class Login(Resource):
    def get(self):
        return make_response(render_template("login.html"), 200)
    def post(self):
        body = request.get_json()
        user = User(**body)
