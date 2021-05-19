from flask import flash, make_response, redirect, render_template, url_for
from flask_restful import Resource
from src import db
from src.database.models import Department as DepartmentModel
from src.database.models import Role, User, UserDepartmentRole
from src.token import token_required, user_return


class Department(Resource):
    """
    Department resource
    Сontains department info
    Requires uuid user as uuid
    Authentication is required
    """
    @token_required
    def get(self, uuid = None):
        """
        Get method
        Return "chat.html" with auth flag, current user obj, department object and dict with user obj and role data
        In case of exception can return main page
        """

        #get department obj bu uuid in link
        department_obj = db.session.query(DepartmentModel).filter_by(uuid = uuid).first()
        if not uuid or not department_obj:
            #return main page
            flash("Not such a department",category='danger')
            return redirect(url_for('main'))
        #take current session user
        current_user = user_return()
        #get all users that in current department
        dep_users = db.session.query(User).join(UserDepartmentRole).join(DepartmentModel).filter(DepartmentModel.uuid == uuid).all()
        #adding users and their roles in dict
        users_and_roles = {}
        for x in dep_users:
            roles = db.session.query(Role).join(UserDepartmentRole).join(DepartmentModel).join(User).filter(User.uuid==x.uuid).filter(DepartmentModel.uuid==uuid).all()
            users_and_roles[x] = roles
        #return department with necessary info
        return make_response(render_template("department.html",auth=True, user=current_user,department_obj = department_obj,users_and_roles=users_and_roles), 200)
