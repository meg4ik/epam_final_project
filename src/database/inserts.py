from src import db
from src.database.models import Department, Role, User, UserDepartmentRole


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
