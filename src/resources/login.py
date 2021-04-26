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
        token = request.cookies.get('token')
        if token:
            try:
                uuid = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])['user_id']
                user = User.query.filter_by(uuid = uuid).first()
            except:
                return make_response(render_template("login.html"), 200)
            flash('You already authorized', category='warning')
            return redirect(url_for('main'))
        return make_response(render_template("login.html"), 200)
            
    def post(self):
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

        response = make_response(redirect(url_for('main')))
        response.set_cookie('token', token)
        return response

class Logout(Resource):
    def post(self):
        response = make_response(redirect(url_for('main')))
        response.set_cookie('token', expires=0)
        return response

