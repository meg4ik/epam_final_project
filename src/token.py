from functools import wraps

import jwt
from flask import flash, redirect, request, url_for

from src import app
from src.database.models import User


# token check decorator
def token_required(func):
    """
    Checking for the presence of a token in the context of user work
    Return current route
    Usage:
    @token_required
    def get(self):
        ...
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        #wrapper of current func

        #take csrf-token from cookies
        token = request.cookies.get('token')
        if not token:
            #returning login page
            flash("Authentication required", category='danger')
            return redirect(url_for('login'))
        #decoding token
        try:
            uuid = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])['user_id']
        except:
            #returning login page
            flash("Token timeout", category='danger')
            return redirect(url_for('login'))
        #get current user
        user = User.query.filter_by(uuid=uuid).first()
        if not user:
            #returning login page
            flash("Profile error", category='danger')
            return redirect(url_for('login'))
        return func(self, *args, **kwargs)

    return wrapper

# return current user function
def user_return():
    """
    Return current web context user object
    """

    #take csrf-token from cookies
    token = request.cookies.get('token')
    #decoding token
    uuid = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])['user_id']
    #get current user
    user = User.query.filter_by(uuid=uuid).first()
    return user
