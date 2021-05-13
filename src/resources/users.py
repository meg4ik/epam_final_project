from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request
from src import db
from src.database.models import User

class Users(Resource):
    @token_required
    def get(self, page):
        q = request.args.get('q')
        if page and page.isdigit():
            page = int(page)
        else:
            page = 1
        if q:
            users = db.session.query(User).filter(User.name.contains(q) | User.surname.contains(q))
        else:
            users = db.session.query(User)

        current_user = user_return()
        
        pages = users.paginate(page=page, per_page=8)

        return make_response(render_template("users.html",auth=True, user=current_user,pages=pages))