from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request, flash, redirect, url_for
from src.database.models import User as UserModel, Role, UserDepartmentRole, Department
from src import db
from flask_bcrypt import generate_password_hash

class User(Resource):
    """
    User resource
    Сontains user info
    Requires uuid user as uuid
    Authentication is required
    """
    @token_required
    def get(self, uuid = None):
        #get user obj bu uuid in link
        user_obj = db.session.query(UserModel).filter_by(uuid = uuid).first()
        if not uuid or not user_obj:
            flash("Not such a user",category='danger')
            return redirect(url_for('main'))
        current_user = user_return()
        departments = db.session.query(Department).join(UserDepartmentRole).join(UserModel).filter(UserModel.uuid==uuid).all() 
        dep_and_roles = {}
        for x in departments:
            roles = db.session.query(Role).join(UserDepartmentRole).join(Department).join(UserModel).filter(UserModel.uuid==uuid).filter(Department.uuid==x.uuid).all()
            dep_and_roles[x] = roles
        if current_user.is_admin:
            sum_of_paycheck = 0
            paycheck_list = db.session.query(UserDepartmentRole).join(UserModel).filter(UserDepartmentRole.user_id==user_obj.id).all()
            for i in paycheck_list:
                role = db.session.query(Role).filter(Role.id == i.role_id).first()
                sum_of_paycheck += role.paycheck
            return make_response(render_template("user.html",auth=True, user=current_user, user_view = user_obj, dep_and_roles = dep_and_roles, sum_of_paycheck=sum_of_paycheck), 200)
        else: 
            return make_response(render_template("user.html",auth=True, user=current_user, dep_and_roles = dep_and_roles, user_view = user_obj), 200)
    @token_required
    def put(self, uuid):
        current_user = user_return()
        if current_user.is_admin:
            user = db.session.query(UserModel).filter_by(uuid = uuid).first()
            if not user:
                flash("Not such a user",category='danger')
                return redirect(url_for('main'))
            try:
                db.session.query(UserModel).filter_by(uuid = uuid).update(
                    dict(
                        username=request.form.get('username'),
                        name=request.form.get('name'),
                        surname=request.form.get('surname'),
                        email_address=request.form.get('email_address')
                    )
                )
                if 'password' in request.form.to_dict():
                    db.session.query(UserModel).filter_by(uuid = uuid).update(
                    dict(
                        password=generate_password_hash(request.form.get('password')).decode('utf8'))
                    )

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
                user.save_to_db()
                flash("Update was successful",category='danger')
            except (ValueError, KeyError) as e:
                flash("Wrong data",category='danger')
                return redirect(url_for('main'))
        else:
            flash("No permission for this page",category='danger')
            return redirect(url_for('main'))
    @token_required
    def delete(self, uuid):
        current_user = user_return()
        if current_user.is_admin:
            user = db.session.query(UserModel).filter_by(uuid = uuid).first()
            db.session.delete(user)
            db.session.commit()
            flash("Deletion was successful",category='danger')
        else:
            flash("No permission for this page",category='danger')
            return redirect(url_for('main'))
