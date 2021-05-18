from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request
from src import db
from src.database.models import User

class Users(Resource):
    """
    Users resource
    Сontains all users
    Requires page for pagination
    Authentication is required
    """
    @token_required
    def get(self, page):
        """
        Get method
        Return "users.html" with auth flag, current user obj and pagination page
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
            users = db.session.query(User).filter(User.name.contains(q) | User.surname.contains(q))
        else:
            # take all users
            users = db.session.query(User)
        # take current session user
        current_user = user_return()
        # make paginaton on database
        pages = users.paginate(page=page, per_page=8)
        # return users.html
        return make_response(render_template("users.html",auth=True, user=current_user,pages=pages), 200)