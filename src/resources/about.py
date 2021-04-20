from flask_restful import Resource
from flask import render_template, make_response

class About(Resource):
    def get(self):
        return make_response(render_template("about.html"), 200)