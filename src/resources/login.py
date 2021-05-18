import datetime
import jwt
import datetime

from flask import (flash, make_response, redirect, render_template, request,
                   url_for, make_response)
from flask_restful import Resource
from src import app
from src.database.models import User


class Login(Resource):
    """
    Login resource
    Сontains login form
    Authentication is not required and shouldn't be done
    """
    def get(self):
        """
        Get method
        Return "login.html"
        In case of exception can return main page
        """

        #take csrf-token from cookies
        token = request.cookies.get('token')
        if token:
            # try decoding token and getting current user
            try:
                uuid = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[
                                  "HS256"])['user_id']
                user = User.query.filter_by(uuid=uuid).first()
            except:
                #return login page
                return make_response(render_template("login.html"), 419)
            flash('You already authorized', category='warning')
            return redirect(url_for('main'))
            #return login page
        return make_response(render_template("login.html"), 200)

    def post(self):
        """
        Post method
        Return redirect to "main.html" if session joining was successful
        In case of exception can return login page
        """

        #take data from responce form
        auth = request.form.to_dict()
        #get user with from key "username"
        user = User.query.filter_by(username=auth.get('username')).first()
        #if user or user hash are not match
        if not user or not user.check_password(auth.get('password')):
            flash('Username and password are not match! Please try again',
                  category='danger')
            #returning redirect login
            return redirect(url_for('login'))
        #make csrf code by jwt algorithm
        token = jwt.encode(
            {
                "user_id": user.uuid,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
            }, app.config['SECRET_KEY'], algorithm="HS256"
        )

        flash('You have been authorized', category='success')
        #set cookie token and return main page
        response = make_response(redirect(url_for('main')))
        response.set_cookie('token', token)
        return response


class Logout(Resource):
    """
    Logout resource
    Set token expires as zero
    It makes csrf token irrelevant
    """
    def post(self):
        """
        Post method
        Return redirect to "main.html"
        Вe-actualizes csrf token in cookie
        """
        response = make_response(redirect(url_for('main')))
        response.set_cookie('token', expires=0)
        return response
