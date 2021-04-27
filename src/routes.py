from src import api
from src.resources.main import Main
from src.resources.about import About
from src.resources.login import Login, Logout
#from src.resources.signup import Signup
#from src.resources.user import UserRes
from src.resources.profile import Profile

api.add_resource(Main, '/', '/main', strict_slashes=False)
api.add_resource(About, '/about', strict_slashes=False)
api.add_resource(Login, '/login', strict_slashes=False)
#api.add_resource(Signup, '/signup', strict_slashes=False)
api.add_resource(Logout, '/logout', strict_slashes=False)
#api.add_resource(UserRes, '/user/<uuid>', strict_slashes=False)
api.add_resource(Profile, '/profile', strict_slashes=False)
