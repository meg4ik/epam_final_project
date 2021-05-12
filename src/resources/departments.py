from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request
from src import db
from src.database.models import Department

class Departments(Resource):
    @token_required
    def get(self):
        q = request.args.get('q')
        if q:
            departments = db.session.query(Department).filter(Department.title.contains(q) | Department.description.contains(q)).all()
        else:
            departments = db.session.query(Department).all()

        current_user = user_return()
        
        return make_response(render_template("departments.html",auth=True, user=current_user,departments = departments))