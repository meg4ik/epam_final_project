import secrets
# python wsgi.py --settings=configs.common_debug
DEBUG = False

SECRET_KEY = secrets.token_hex(16)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:totalmag@localhost/department_project'

SQLALCHEMY_TRACK_MODIFICATIONS = False
