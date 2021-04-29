import jwt
from functools import wraps
from flask import request, redirect, url_for, flash
from src.database.models import User
from src import app

def token_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            flash("Authentication required", category='danger')
            return redirect(url_for('login'))
        try:
            uuid = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])['user_id']
        except:
            flash("Token timeout", category='danger')
            return redirect(url_for('login'))
        user = User.query.filter_by(uuid=uuid).first()
        if not user:
            flash("Profile error", category='danger')
            return redirect(url_for('login'))
        return func(self, *args, **kwargs)

    return wrapper

def user_return():
    token = request.cookies.get('token')
    uuid = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])['user_id']
    user = User.query.filter_by(uuid=uuid).first()
    return user