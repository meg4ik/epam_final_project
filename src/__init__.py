from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from simple_settings import settings

__author__ = 'Pavlo Ryndin'

app = Flask(__name__, static_url_path='', static_folder='src/static', template_folder='src/templates')

try:
    app.config.update(**settings.as_dict())
except:
    print ("Please configurate your environment!")

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src import routes