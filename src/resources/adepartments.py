from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request, flash, redirect, url_for
from src.database.models import Department
from src import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from src.schemas.department import DepartmentSchema

class Adepartments(Resource):
    @token_required
    def get(self):
        current_user = user_return()
        if current_user.is_admin:
            departments = db.session.query(Department).all()
            return make_response(render_template("adepartments.html",auth=True, user=current_user, departments=departments), 200)
        else:
            flash("No permission for this page",category='danger')
            return redirect(url_for('main'))
    @token_required
    def post(self):
        current_user = user_return()
        if current_user.is_admin:
            department_schema = DepartmentSchema()
            print(request.form.to_dict())
            try:
                department = department_schema.load(request.form.to_dict(), session=db.session)
            except ValidationError as e:
                flash(e.normalized_messages()[[*e.normalized_messages()][0]][0],category='danger')
                return redirect(url_for('adepartments'))
            else:
                try:
                    department.save_to_db()
                except IntegrityError:
                    flash("Such department exists",category='warning')
                    return redirect(url_for('adepartment'))
                else:
                    flash('Department created successfully!',category='success')
                    return redirect(url_for('adepartments'))
        else:
            flash("No permission for this method",category='danger')
            return redirect(url_for('main'))