import secrets
#python wsgi.py --settings=configs.common_deploy
DEBUG=False

secret_key = secrets.token_hex(16)
SECRET_KEY=secret_key

WTF_CSRF_ENABLED=False

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:totalmag@localhost/guest_book'
#TODO
#логин пароль на базу данных переделать на скрытый тип
SQLALCHEMY_TRACK_MODIFICATIONS = False