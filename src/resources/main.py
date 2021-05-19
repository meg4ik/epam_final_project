import jwt
from flask import make_response, render_template, request
from flask_restful import Resource
from src import app
from src.database.models import User


class Main(Resource):
    """
    Main resource
    Сontains main page info
    Authentication is not required
    """
    def get(self):
        """
        Get method
        Return "departments.html" with auth flag, current user uuid and current user
        In case of exception can return main page
        """

        #take csrf-token from cookies
        token = request.cookies.get('token')
        try:
            #decoding token
            uuid = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[
                              "HS256"])['user_id']
            #get user
            user = User.query.filter_by(uuid=uuid).first()
        except:
            # return page with no user session
            return make_response(render_template("main.html", auth=None, uuid=None, user=None), 200)
        # return page in user session
        return make_response(render_template("main.html", auth=True, uuid=uuid, user=user), 202)
