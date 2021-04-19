from src import api
from src.resources.main import Main

api.add_resource(Main, '/', '/main', strict_slashes=False)