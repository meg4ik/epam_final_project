from flask_restful import Resource
from flask import render_template, make_response, request, redirect, url_for
from src.database.models import User
import jwt
from src import app


class Main(Resource):
    def get(self):
        token = request.cookies.get('token')
        try:
            uuid = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[
                              "HS256"])['user_id']
            user = User.query.filter_by(uuid=uuid).first()
        except:
            return make_response(render_template("main.html", auth=None, uuid=None, user=None), 200)
        return make_response(render_template("main.html", auth=True, uuid=uuid, user=user), 202)
