from src import api
from src.resources.main import Main
from src.resources.about import About
from src.resources.login import Login, Logout
from src.resources.profile import Profile
from src.resources.user import User
from src.resources.department import Department
from src.resources.users import Users
from src.resources.departments import Departments
from src.resources.chats import Chats
from src.resources.chat import Chat

from src import app
from flask import render_template

#
# Declarations of app routes in type of rest web-architecture
#

# routes
api.add_resource(Main, '/', '/main', strict_slashes=False)
api.add_resource(About, '/about', strict_slashes=False)
api.add_resource(Login, '/login', strict_slashes=False)
api.add_resource(Logout, '/logout', strict_slashes=False)
api.add_resource(Profile, '/profile', strict_slashes=False)
api.add_resource(User, '/user/<uuid>', strict_slashes=False)
api.add_resource(Department, '/department/<uuid>', strict_slashes=False)
api.add_resource(Users, '/users/<page>', strict_slashes=False)
api.add_resource(Departments, '/departments/<page>', strict_slashes=False)
api.add_resource(Chats, '/chats', strict_slashes=False)
api.add_resource(Chat, '/chat/<uuid_to>', strict_slashes=False)

# handling of 404 page error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
