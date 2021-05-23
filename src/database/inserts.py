from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid

from flask_bcrypt import generate_password_hash


app = Flask(__name__)
db = SQLAlchemy(app)

database_pass = "qwerty"
shema_link = "localhost/department_project"

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://db_user:{}@{}'.format(database_pass, shema_link)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



class UserDepartmentRole(db.Model):
    """
    UserDepartmentRole model
    """
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

class Message(db.Model):
    """
    Message model
    """
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    user_id_from = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_id_to = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    prev_message_id = db.Column(db.Integer)
    text = db.Column(db.String(100), nullable=False)

    user_from = db.relationship("User", foreign_keys=[user_id_from])
    user_to = db.relationship("User", foreign_keys=[user_id_to])

    def __init__(self, user_id_from, user_id_to, prev_message_id, text):
        self.user_id_from = user_id_from
        self.user_id_to = user_id_to
        self.prev_message_id = prev_message_id
        self.text = text

class User(db.Model):
    """
    User model
    """
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


class Role(db.Model):
    """
    Role model
    """
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False, unique=True)
    paycheck = db.Column(db.Integer, nullable=False)
    user_department_role_to = db.relationship("UserDepartmentRole",backref='role',lazy=True)

    def __init__(self, title, paycheck):
        self.title = title
        self.paycheck = paycheck


class Department(db.Model):
    """
    Department model
    """
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


def finsert():
    us1 = User(
        username="user9474",
        name="Dmitrii",
        surname="Abdulov",
        email_address="dmabd@gmail.com",
        password="passofuser9474",
        is_admin=True
        )
    us2 = User(
        username="user0011",
        name="Pavlo",
        surname="Kotza",
        email_address="pako@gmail.com",
        password="passofuser0011",
        is_admin=False
        )
    us3 = User(
        username="user7433",
        name="Krass",
        surname="Mazov",
        email_address="krmaz@gmail.com",
        password="passofuser7433",
        is_admin=False
        )
    us4 = User(
        username="user9284",
        name="Genadii",
        surname="Doritas",
        email_address="gdor@gmail.com",
        password="passofuser9284",
        is_admin=False
        )
    us5 = User(
        username="user5566",
        name="Margo",
        surname="Nusso",
        email_address="manu@gmail.com",
        password="passofuser5566",
        is_admin=False
        )
    us6 = User(
        username="user8989",
        name="Alex",
        surname="Gvido",
        email_address="algv@gmail.com",
        password="passofuser8989",
        is_admin=False)
    us7 = User(
        username="3843",
        name="Urii",
        surname="Maslov",
        email_address="urma@gmail.com",
        password="passofuser3843",
        is_admin=False
        )
    us8 = User(
        username="3335",
        name="Alfreds",
        surname="Futterkiste",
        email_address="alfu@gmail.com",
        password="passofuser3335",
        is_admin=False
        )
    us9 = User(
        username="3475",
        name="Drachenblut",
        surname="Delikatessend",
        email_address="drde@gmail.com",
        password="passofuser3475",
        is_admin=False
        )
    us10 = User(
        username="0343",
        name="Ernst",
        surname="Handel",
        email_address="erha@gmail.com",
        password="passofuser0343",
        is_admin=False
        )
    role1 = Role(
        title="Junior dev",
        paycheck=300
        )
    role2 = Role(
        title="Middle dev",
        paycheck=1000
        )
    role3 = Role(
        title="Senior dev",
        paycheck=2500
        )
    role4 = Role(
        title="Lead dev",
        paycheck=4000
        )
    role5 = Role(
        title="Designer",
        paycheck=500
        )
    dep1 = Department(
        title="Flappy bird clone game",
        description="Crossplatform arcade game"
        )
    dep2 = Department(
        title="Music web app",
        description="WebApp for listening music"
        )
    dep3 = Department(
        title="Bank blockchain",
        description="Blockchain alghorithms for internal bank system"
        )
    
    db.session.add(us1)
    db.session.add(us2)
    db.session.add(us3)
    db.session.add(us4)
    db.session.add(us5)
    db.session.add(us6)
    db.session.add(us7)
    db.session.add(us8)
    db.session.add(us9)
    db.session.add(us10)

    db.session.add(role1)
    db.session.add(role2)
    db.session.add(role3)
    db.session.add(role4)
    db.session.add(role5)

    db.session.add(dep1)
    db.session.add(dep2)
    db.session.add(dep3)

    udr1 = UserDepartmentRole(
        user=db.session.query(User).filter(User.username == us2.username).first(),
        department=db.session.query(Department).filter(Department.title == dep1.title).first(),
        role=db.session.query(Role).filter(Role.title == role1.title).first()
        )
    udr2 = UserDepartmentRole(
        user=db.session.query(User).filter(User.username == us3.username).first(),
        department=db.session.query(Department).filter(Department.title == dep1.title).first(),
        role=db.session.query(Role).filter(Role.title == role1.title).first()
        )
    udr3 = UserDepartmentRole(
        user=db.session.query(User).filter(User.username == us3.username).first(),
        department=db.session.query(Department).filter(Department.title == dep2.title).first(),
        role=db.session.query(Role).filter(Role.title == role2.title).first()
        )
    udr4 = UserDepartmentRole(
        user=db.session.query(User).filter(User.username == us4.username).first(),
        department=db.session.query(Department).filter(Department.title == dep1.title).first(),
        role=db.session.query(Role).filter(Role.title == role2.title).first()
        )
    udr5 = UserDepartmentRole(
        user=db.session.query(User).filter(User.username == us4.username).first(),
        department=db.session.query(Department).filter(Department.title == dep2.title).first(),
        role=db.session.query(Role).filter(Role.title == role2.title).first()
        )
    udr6 = UserDepartmentRole(
        user=db.session.query(User).filter(User.username == us4.username).first(),
        department=db.session.query(Department).filter(Department.title == dep3.title).first(),
        role=db.session.query(Role).filter(Role.title == role5.title).first()
        )
    udr7 = UserDepartmentRole(
        user=db.session.query(User).filter(User.username == us5.username).first(),
        department=db.session.query(Department).filter(Department.title == dep1.title).first(),
        role=db.session.query(Role).filter(Role.title == role5.title).first()
        )
    udr8 = UserDepartmentRole(
        user=db.session.query(User).filter(User.username == us5.username).first(),
        department=db.session.query(Department).filter(Department.title == dep2.title).first(),
        role=db.session.query(Role).filter(Role.title == role1.title).first()
        )
    udr9 = UserDepartmentRole(
        user=db.session.query(User).filter(User.username == us6.username).first(),
        department=db.session.query(Department).filter(Department.title == dep3.title).first(),
        role=db.session.query(Role).filter(Role.title == role4.title).first()
        )

    db.session.add(udr1)
    db.session.add(udr2)
    db.session.add(udr3)
    db.session.add(udr4)
    db.session.add(udr5)
    db.session.add(udr6)
    db.session.add(udr7)
    db.session.add(udr8)
    db.session.add(udr9)

    db.session.commit()
    db.session.close()

def insert_run():
    """
    Inserting information into a database
    """
    print("Start inserting")
    try:
        finsert()
    except Exception as e:
        print(e)
    else:
        print("Completed successfully")

insert_run()