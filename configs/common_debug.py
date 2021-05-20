import secrets
# python wsgi.py --settings=configs.common_debug
DEBUG = True

RUN_INSERT = False

SECRET_KEY = secrets.token_hex(16)

database_pass = "totalmag"
shema_link = "localhost/department_project"

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@{}'.format(database_pass, shema_link)

SQLALCHEMY_TRACK_MODIFICATIONS = False
