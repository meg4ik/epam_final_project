from src import api
from src.resources.main import Main
from src.resources.about import About
from src.resources.login import Login

api.add_resource(Main, '/', '/main', strict_slashes=False)
api.add_resource(About, '/about', strict_slashes=False)
api.add_resource(Login, '/login', strict_slashes=False)