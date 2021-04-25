import datetime
import jwt
import datetime

from flask import (flash, make_response, redirect, render_template, request,
                   url_for, make_response)
from flask_restful import Resource
from src import app
from src.database.models import User


class Login(Resource):
    def get(self):
        if not auth:
            return make_response(render_template("login.html"), 200)
        flash('You already authorized', category='warning')
        return redirect(url_for('main'))
       
    def post(self):
        if request.authorization:
            flash('You allready authorizated', category='danger')
            return redirect(url_for('main'))
        auth = request.form.to_dict()
        user = User.query.filter_by(username=auth.get('username')).first()
        if not user or not user.check_password(auth.get('password')):
            flash('Username and password are not match! Please try again', category='danger')
            return redirect(url_for('login'))
        token = jwt.encode(
            {
                "user_id": user.uuid,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
            }, app.config['SECRET_KEY']
            , algorithm="HS256"
        )

        flash('You have been authorized', category='success')

        response = make_response(render_template("main.html"))
        response.set_cookie('token', token)
        return response

class Logout(Resource):
    def post():
        return redirect(url_for('main'))

