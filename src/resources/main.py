from flask_restful import Resource
from flask import render_template, make_response

class Main(Resource):
    def get(self):
        return make_response(render_template("main.html"), 200)
