from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from simple_settings import settings

from os import path

__author__ = 'Pavlo Ryndin'

temp_dir = path.abspath(path.dirname(__file__))
app = Flask(__name__, static_folder=path.join(temp_dir, 'static'), template_folder=path.join(temp_dir, 'templates'))

# try:
#     app.config.update(**settings.as_dict())
# except:
#     print ("Please configurate your environment!")
app.config.from_pyfile(path.join(path.dirname(temp_dir),'configs','common_debug.py'))

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src import routes
from src.database import models