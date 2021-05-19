from flask import make_response, render_template
from flask_restful import Resource
from src import db
from src.database.models import Department, Role, User, UserDepartmentRole
from src.token import token_required, user_return


class Profile(Resource):
    """
    Profile resource
    Сontains current session user page
    Authentication is required
    """
    @token_required
    def get(self):
        """
        Get method
        Return "profile.html" with auth flag, sum of paycheck, current user, dict with department and list of roles data
        """

        #take current session user
        current_user = user_return()
        #check user status
        if current_user.is_admin:
            #return admin profile page
            return make_response(render_template("profile.html",auth=True, user=current_user), 200)
        else:
            #calculating sum of user paychecks from all roles in departments
            sum_of_paycheck = 0
            paycheck_list = db.session.query(UserDepartmentRole).join(User).filter(UserDepartmentRole.user_id==current_user.id).all()
            for i in paycheck_list:
                role = db.session.query(Role).filter(Role.id == i.role_id).first()
                sum_of_paycheck += role.paycheck
            #make dict with department and list of roles data
            departments = db.session.query(Department).join(UserDepartmentRole).join(User).filter(User.uuid==current_user.uuid).all() 
            dep_and_roles = {}
            for x in departments:
                roles = db.session.query(Role).join(UserDepartmentRole).join(Department).join(User).filter(User.uuid==current_user.uuid).filter(Department.uuid==x.uuid).all()
                dep_and_roles[x] = roles
            # return profile 
            return make_response(render_template("profile.html",auth=True,sum_of_paycheck=sum_of_paycheck, user=current_user, dep_and_roles = dep_and_roles), 200)
