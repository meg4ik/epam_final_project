from flask_restful import Resource
from flask import render_template

class Main(Resource):
    def get(self):
        return render_template("main.html")