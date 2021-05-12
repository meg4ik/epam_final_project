from src import api
from src.resources.main import Main
from src.resources.about import About
from src.resources.login import Login, Logout
from src.resources.profile import Profile
from src.resources.user import User
from src.resources.department import Department
from src.resources.users import Users
from src.resources.departments import Departments

api.add_resource(Main, '/', '/main', strict_slashes=False)
api.add_resource(About, '/about', strict_slashes=False)
api.add_resource(Login, '/login', strict_slashes=False)
api.add_resource(Logout, '/logout', strict_slashes=False)
api.add_resource(Profile, '/profile', strict_slashes=False)
api.add_resource(User, '/user/<uuid>', strict_slashes=False)
api.add_resource(Department, '/department/<uuid>', strict_slashes=False)
api.add_resource(Users, '/users', strict_slashes=False)
api.add_resource(Departments, '/departments', strict_slashes=False)
