from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request, flash, redirect, url_for
from src.database.models import User
from src import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from src.schemas.user import UserSchema

class Ausers(Resource):
    @token_required
    def get(self):
        current_user = user_return()
        if current_user.is_admin:
            users = db.session.query(User).all()
            return make_response(render_template("ausers.html",auth=True, user=current_user, users=users), 200)
        else:
            flash("No permission for this page",category='danger')
            return redirect(url_for('main'))
    @token_required
    def post(self):
        current_user = user_return()
        if current_user.is_admin:
            user_schema = UserSchema()
            try:
                user = user_schema.load(request.form.to_dict(), session=db.session)
            except ValidationError as e:
                flash(e.normalized_messages()['_schema'][0],category='danger')
                return redirect(url_for('ausers'))
            else:
                try:
                    user.save_to_db()
                except IntegrityError:
                    flash("Such user exists",category='warning')
                    return redirect(url_for('ausers'))
                else:
                    flash('Account created successfully!',category='success')
                    return redirect(url_for('ausers'))
        else:
            flash("No permission for this method",category='danger')
            return redirect(url_for('main'))