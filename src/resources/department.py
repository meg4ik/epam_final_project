from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request, flash, redirect, url_for, abort
from src.database.models import User, Role, UserDepartmentRole, Department as DepartmentModel
from src import db

class Department(Resource):
    @token_required
    def get(self, uuid = None):
        department_obj = db.session.query(DepartmentModel).filter_by(uuid = uuid).first()
        if not uuid or not department_obj:
            flash("Not such a department",category='danger')
            return redirect(url_for('main'))
        current_user = user_return()
        dep_users = db.session.query(User).join(UserDepartmentRole).join(DepartmentModel).filter(DepartmentModel.uuid == uuid).all()
        users_and_roles = {}
        for x in dep_users:
            roles = db.session.query(Role).join(UserDepartmentRole).join(DepartmentModel).join(User).filter(User.uuid==x.uuid).filter(DepartmentModel.uuid==uuid).all()
            users_and_roles[x] = roles
        if current_user.is_admin:
            pass
            # paycheck_list = db.session.query(Role).join(UserDepartmentRole).join(UserModel).filter(UserModel.uuid==uuid).all()
            # sum_of_paycheck = sum([x.paycheck for x in paycheck_list])
            #return make_response(render_template("department.html",auth=True, user=current_user, user_view = user_obj, dep_and_roles = dep_and_roles, sum_of_paycheck=sum_of_paycheck), 200)
        else: 
            return make_response(render_template("department.html",auth=True, user=current_user,department_obj = department_obj,users_and_roles=users_and_roles), 200)