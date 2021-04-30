from src import api
from src.resources.main import Main
from src.resources.about import About
from src.resources.login import Login, Logout
from src.resources.profile import Profile
from src.resources.ausers import Ausers
from src.resources.adepartments import Adepartments

api.add_resource(Main, '/', '/main', strict_slashes=False)
api.add_resource(About, '/about', strict_slashes=False)
api.add_resource(Login, '/login', strict_slashes=False)
api.add_resource(Logout, '/logout', strict_slashes=False)
api.add_resource(Profile, '/profile', strict_slashes=False)
api.add_resource(Ausers, '/admin/users', strict_slashes=False)
api.add_resource(Adepartments, '/admin/departments', strict_slashes=False)
