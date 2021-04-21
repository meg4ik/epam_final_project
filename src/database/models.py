from src import db
from flask_bcrypt import generate_password_hash, check_password_hash
import uuid

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),nullable=False, unique=True)
    name = db.Column(db.String(30),nullable=False)
    surname = db.Column(db.String(30),nullable=False)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    uuid = db.Column(db.String(36), unique=True)

    def __init__(self, username, name, surname, email_address, password, is_admin):
        self.username = username
        self.name = name
        self.surname = surname
        self.email_address = email_address
        self.password = generate_password_hash(password).decode('utf8')
        self.is_admin = is_admin
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f'User({self.surname}, {self.name})'

    def check_password(self, attempted_password):
        return check_password_hash(self.password, attempted_password)

class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)