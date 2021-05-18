from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request
from src import db
from src.database.models import Department


class Departments(Resource):
    """
    Departments resource
    Сontains all departments
    Requires page for pagination
    Authentication is required
    """
    @token_required
    def get(self, page):
        """
        Get method
        Return "departments.html" with auth flag, current user obj and pagination page
        """

        # get response with search text
        q = request.args.get('q')
        # formatting number
        if page and page.isdigit():
            page = int(page)
        else:
            page = 1
        # if there any seaching text
        if q:
            # take result of searching
            departments = db.session.query(Department).filter(
                Department.title.contains(q) | Department.description.contains(q))
        else:
            # take all departments
            departments = db.session.query(Department)
        # take current session user
        current_user = user_return()
        # make paginaton on database
        pages = departments.paginate(page=page, per_page=8)
        # return departments.html
        return make_response(render_template("departments.html", auth=True, user=current_user, pages=pages), 200)
