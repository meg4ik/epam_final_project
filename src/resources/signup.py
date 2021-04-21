from flask_restful import Resource
from flask import render_template, make_response, request, flash
from src.database.models import User
from src.schemas.user import UserSchema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from src import db

class Signup(Resource):
    user_schema = UserSchema()
    def get(self):
        return make_response(render_template("signup.html"), 200)
    def post(self):
        try:
            user = self.user_schema.load(request.json, session=db.session)
        except ValidationError as e:
            flash(e)
        else:
            try:
                db.session.add(user)
                db.session.commit()
            except IntegrityError:
                flash("Such user exists")
            else:
                return self.user_schema.dump(user), 201