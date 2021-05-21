import src
from src import app, db
from src.database.models import User

from tests.tokens import set_token

client = app.test_client()

def test_get_user_route_auth_not_admin():
    """
    Testing user page with user session as not admin
    Method : GET
    """
    user =  db.session.query(User).filter(User.username == "user7433").first()
    url = '/user/{}'.format(user.uuid)
    set_token(client, "user0011")

    response = client.get(url)
    assert response.status_code == 200

def test_get_user_route_auth_admin():
    """
    Testing user page with user session as admin
    Method : GET
    """
    user =  db.session.query(User).filter(User.username == "user7433").first()
    url = '/user/{}'.format(user.uuid)
    set_token(client, "user9474")

    response = client.get(url)
    assert response.status_code == 200

def test_get_wrong_user_route():
    """
    Testing user page with wrong uuid
    Method : GET
    """
    url = '/user/{}'.format("1111")
    set_token(client, "user9474")

    response = client.get(url)
    assert response.status_code == 302

def test_put_user_route_wrong_data_auth_admin():
    """
    Testing put page with wrong data
    Method : PUT
    """
    user =  db.session.query(User).filter(User.username == "user7433").first()
    url = '/user/{}'.format(user.uuid)
    set_token(client, "user9474")

    resp_dict = {"username":"test", "name":"test", "surname":"test", "email_address":"test"}
    response = client.put(url, data=resp_dict)
    assert response.status_code == 302

def test_put_wrong_user_route():
    """
    Testing user page with wrong uuid
    Method : PUT
    """
    url = '/user/{}'.format("1111")
    set_token(client, "user9474")
    resp_dict = {"username":"test", "name":"test", "surname":"test", "email_address":"test"}
    response = client.put(url, data=resp_dict)
    assert response.status_code == 302

def test_put_user_with_user_session_as_not_admin():
    """
    Testing user page with user session as not admin
    Method : PUT
    """
    user =  db.session.query(User).filter(User.username == "user7433").first()

    resp_dict = {"username":"test", "name":"test", "surname":"test", "email_address":"test"}
    url = '/user/{}'.format(user.uuid)
    set_token(client, "user0011")

    response = client.put(url, data=resp_dict)
    assert response.status_code == 302

def test_delete_user_with_user_session_as_not_admin():
    """
    Testing delete user page with user session as not admin
    Method : DELETE
    """
    user =  db.session.query(User).filter(User.username == "user7433").first()

    url = '/user/{}'.format(user.uuid)
    set_token(client, "user0011")

    response = client.delete(url)
    assert response.status_code == 302