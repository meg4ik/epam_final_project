from flask_restful import Resource
from flask import render_template, make_response, request
from src.database.models import User
import jwt
from src import app


class About(Resource):
    """
    About resource
    Сontains common information about project
    Authentication is not required
    """
    def get(self):
        """
        Get method
        Return "about.html" with current user obj
        In case if there not user session return page with no authentication
        """
        #take csrf-token from cookies
        token = request.cookies.get('token')
        #decoding token
        try:
            uuid = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[
                              "HS256"])['user_id']
            #get current user
            user = User.query.filter_by(uuid=uuid).first()
        except:
            # return page with no user session
            return make_response(render_template("about.html", auth=None, uuid=None, user=None), 200)
        # return page in user session
        return make_response(render_template("about.html", auth=True, uuid=uuid, user=user), 202)
