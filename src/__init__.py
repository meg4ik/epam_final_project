from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from simple_settings import settings
from logging import FileHandler, WARNING

from os import path

#
# Setting and adding the required variables
#

__author__ = 'Pavlo Ryndin'

#configuring paths of templates and static
temp_dir = path.abspath(path.dirname(__file__))
app = Flask(__name__, static_folder=path.join(temp_dir, 'static'),
            template_folder=path.join(temp_dir, 'templates'))

#configurating environment
try:
    app.config.update(**settings.as_dict())
except:
    print("Please configurate your environment!")
# app.config.from_pyfile(path.join(path.dirname(
#     temp_dir), 'configs', 'common_debug.py'))

#services declarations
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

from src.database.admin_view import AdminIndexView
admin = Admin(app, index_view=AdminIndexView(), template_mode='bootstrap3')

from src.database.models import User, Department, Role, UserDepartmentRole
from src.database.admin_view import UserModelView, DepartmentModelView
admin.add_views(UserModelView(User, db.session,category="model"), DepartmentModelView(Department, db.session,category="model"), ModelView(Role, db.session,category="model"), ModelView(UserDepartmentRole, db.session,category="model"))

#insert of database info
if app.config['RUN_INSERT']:
    from src.database.inserts import insert_run
    insert_run()

#logging customization
if not app.config['DEBUG']:
    file_error_handler = FileHandler('logs/errorlog.txt')
    file_error_handler.setLevel(WARNING)
    app.logger.addHandler(file_error_handler)

from src import routes
from src.database import models