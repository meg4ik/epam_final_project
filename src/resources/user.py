from flask import (flash, make_response, redirect, render_template, request,
                   url_for)
from flask_bcrypt import generate_password_hash
from flask_restful import Resource
from src import db
from src.database.models import Department, Role
from src.database.models import User as UserModel
from src.database.models import UserDepartmentRole
from src.token import token_required, user_return


class User(Resource):
    """
    User resource
    Сontains user info
    Requires uuid user as uuid
    Authentication is required
    """
    @token_required
    def get(self, uuid = None):
        """
        Get method
        Return "user.html" with auth flag, current user obj, user view info and paycheck
        In case of exception can return main page
        """

        #get user obj bu uuid in link
        user_obj = db.session.query(UserModel).filter_by(uuid = uuid).first()
        if not uuid or not user_obj:
            #return main page
            flash("Not such a user",category='danger')
            return redirect(url_for('main'))
        #take current session user
        current_user = user_return()
        #take all user departmants
        departments = db.session.query(Department).join(UserDepartmentRole).join(UserModel).filter(UserModel.uuid==uuid).all() 
        #make dict with department and list of roles data
        dep_and_roles = {}
        for x in departments:
            roles = db.session.query(Role).join(UserDepartmentRole).join(Department).join(UserModel).filter(UserModel.uuid==uuid).filter(Department.uuid==x.uuid).all()
            dep_and_roles[x] = roles
        #if user statust admin calculate sum of user paychecks
        if current_user.is_admin:
            sum_of_paycheck = 0
            paycheck_list = db.session.query(UserDepartmentRole).join(UserModel).filter(UserDepartmentRole.user_id==user_obj.id).all()
            for i in paycheck_list:
                role = db.session.query(Role).filter(Role.id == i.role_id).first()
                sum_of_paycheck += role.paycheck
            #return admin user view
            return make_response(render_template("user.html",auth=True, user=current_user, user_view = user_obj, dep_and_roles = dep_and_roles, sum_of_paycheck=sum_of_paycheck), 200)
        else: 
            #return non admin user view
            return make_response(render_template("user.html",auth=True, user=current_user, dep_and_roles = dep_and_roles, user_view = user_obj), 200)
    @token_required
    def put(self, uuid):
        """
        Put method
        Flash alert into user view
        In case of exception can return main page
        """

        #take current session user
        current_user = user_return()
        #if requested user status admin
        if current_user.is_admin:
            #take user obj to update
            user = db.session.query(UserModel).filter_by(uuid = uuid).first()
            #if no such user in db
            if not user:
                flash("Not such a user",category='danger')
                return redirect(url_for('main'))
            try:
                #create query as dict with all info from requested form
                db.session.query(UserModel).filter_by(uuid = uuid).update(
                    dict(
                        username=request.form.get('username'),
                        name=request.form.get('name'),
                        surname=request.form.get('surname'),
                        email_address=request.form.get('email_address')
                    )
                )
                #check on password data
                if 'password' in request.form.to_dict():
                    db.session.query(UserModel).filter_by(uuid = uuid).update(
                    dict(
                        password=generate_password_hash(request.form.get('password')).decode('utf8'))
                    )
                #check on is_admin flag data
                if 'is_admin' in request.form.to_dict():
                    db.session.query(UserModel).filter_by(uuid = uuid).update(
                    dict(
                        is_admin=True
                    ))
                else:
                    db.session.query(UserModel).filter_by(uuid = uuid).update(
                    dict(
                        is_admin=False
                    ))
                #save to db
                user.save_to_db()
                flash("Update was successful",category='danger')
            #something went wrong
            except (ValueError, KeyError) as e:
                flash("Wrong data",category='danger')
                return redirect(url_for('main'))
        else:
            #current session user status is not admin
            flash("No permission for this page",category='danger')
            return redirect(url_for('main'))
    @token_required
    def delete(self, uuid):
        """
        Delete method
        Flash alert into user view
        In case of exception can return main page
        Only for session user with admin status 
        """

        #take current session user
        current_user = user_return()
        #if requested user status admin
        if current_user.is_admin:
            #take current user form view
            user = db.session.query(UserModel).filter_by(uuid = uuid).first()
            #delete user
            db.session.delete(user)
            db.session.commit()
            flash("Deletion was successful",category='danger')
        else:
            #current session user status is not admin
            flash("No permission for this page",category='danger')
            return redirect(url_for('main'))
