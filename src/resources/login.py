import jwt
import datetime
from flask import request, flash
from flask_restful import Resource
from flask import render_template, make_response, request, redirect, url_for
from src.database.models import User
from src import app

class Login(Resource):
    def get(self):
        # auth = request.headersget('X-API-KEY')
        # print(auth)
        if auth:
            flash('You already authorized', category='warning')
            return redirect(url_for('main'))
        return make_response(render_template("login.html"), 200)
    def post(self):
        auth = request.form.to_dict()
        user = User.query.filter_by(username=auth.get('username')).first()
        if not user or not user.check_password(auth.get('password')):
            flash('Username and password are not match! Please try again', category='danger')
            return redirect(url_for('login'))
        # token = jwt.encode(
        #     {
        #         "user_id": user.uuid,
        #         "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
        #     }, app.config['SECRET_KEY']
        )
        flash('You have been authorized', category='success')
        return redirect(url_for('main'))