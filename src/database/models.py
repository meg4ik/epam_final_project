from src import db
from flask_bcrypt import generate_password_hash, check_password_hash
import uuid

class UserDepartmentRole(db.Model):
    __tablename__ = "user_department_role"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)

    __table_args__ = (db.UniqueConstraint(user_id, department_id, role_id),)

    def __init__(self, user, department, role):
        self.user_id = user.id
        self.department_id = department.id
        self.role_id = role.id

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),nullable=False, unique=True)
    name = db.Column(db.String(30),nullable=False)
    surname = db.Column(db.String(30),nullable=False)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean)
    uuid = db.Column(db.String(36), unique=True)
    user_department_role_to = db.relationship("UserDepartmentRole",backref='user',lazy=True)

    def __init__(self, username, name, surname, email_address, password, is_admin=False):
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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False, unique=True)
    paycheck = db.Column(db.Integer, nullable=False)
    user_department_role_to = db.relationship("UserDepartmentRole",backref='role',lazy=True)

    def __init__(self, title, paycheck):
        self.title = title
        self.paycheck = paycheck

    def __repr__(self):
        return f'Role({self.title})'


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False, unique=True)
    description = db.Column(db.String(300), nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    user_department_role_to = db.relationship("UserDepartmentRole",backref='department',lazy=True)

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f'Department({self.title})'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()