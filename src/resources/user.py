from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request, flash, redirect, url_for
from src.database.models import User as UserModel, Role, UserDepartmentRole, Department
from src import db

class User(Resource):
    @token_required
    def get(self, uuid = None):
        user_obj = db.session.query(UserModel).filter_by(uuid = uuid).first()
        if not uuid or not user_obj:
            flash("Not such a user",category='danger')
            return redirect(url_for('main'))
        current_user = user_return()
        if current_user.is_admin:
            return make_response(render_template("user.html",auth=True, user=current_user, user_view = user_obj), 200)
        else: 
            departments = db.session.query(Department).join(UserDepartmentRole).join(UserModel).filter(UserModel.uuid==uuid).all() 
            dep_and_roles = {}
            for x in departments:
                roles = db.session.query(Role).join(UserDepartmentRole).join(Department).join(UserModel).filter(UserModel.uuid==uuid).filter(Department.title==x.title).all()
                dep_and_roles[x.title] = roles
            return make_response(render_template("user.html",auth=True, user=current_user, dep_and_roles = dep_and_roles, user_view = user_obj), 200)
    def post(self, uuid=None):
        print(1)
    def patch(self):
        pass
    def delete(self): 
        pass