from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template
from src.database.models import User, Department,Role,UserDepartmentRole
from src import db

class Profile(Resource):
    @token_required
    def get(self):
        current_user = user_return()
        if current_user.is_admin:
            return make_response(render_template("profile.html",auth=True, user=current_user), 200)
        else:
            paycheck_list = db.session.query(Role).join(UserDepartmentRole).join(User).filter(User.uuid==current_user.uuid).all()
            sum_of_paycheck = sum([x.paycheck for x in paycheck_list])
            departments = db.session.query(Department).join(UserDepartmentRole).join(User).filter(User.uuid==current_user.uuid).all() 
            dep_and_roles = {}
            for x in departments:
                roles = db.session.query(Role).join(UserDepartmentRole).join(Department).join(User).filter(User.uuid==current_user.uuid).filter(Department.uuid==x.uuid).all()
                dep_and_roles[x] = roles
            return make_response(render_template("profile.html",auth=True,sum_of_paycheck=sum_of_paycheck, user=current_user, dep_and_roles = dep_and_roles), 200)