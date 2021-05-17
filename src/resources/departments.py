from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request
from src import db
from src.database.models import Department

class Departments(Resource):
    @token_required
    def get(self, page):
        q = request.args.get('q')
        if page and page.isdigit():
            page = int(page)
        else:
            page = 1
        if q:
            departments = db.session.query(Department).filter(Department.title.contains(q) | Department.description.contains(q))
        else:
            departments = db.session.query(Department)

        current_user = user_return()
        
        pages = departments.paginate(page=page, per_page=8)

        return make_response(render_template("departments.html",auth=True, user=current_user,pages=pages), 200)