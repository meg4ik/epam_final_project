from flask_restful import Resource
from flask import render_template, make_response
from src.token import token_required

class About(Resource):
    def get(self):
        return make_response(render_template("about.html"), 200)