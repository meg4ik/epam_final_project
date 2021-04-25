import secrets
#python wsgi.py --settings=configs.common_debug
DEBUG=True

SECRET_KEY = secrets.token_hex(16)


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:totalmag@localhost/department_project'
#TODO
#логин пароль на базу данных переделать на скрытый тип
SQLALCHEMY_TRACK_MODIFICATIONS = False