import src
from src import app

from tests.tokens import set_token
client = app.test_client()
url = '/login'

def test_get_login_route_without_session():
    """
    Testing login page without user session
    Method : GET
    """
    response = client.get(url)
    assert response.status_code == 200

def test_get_login_route_with_session():
    """
    Testing login page with user session
    Method : GET
    """
    set_token(client, "user9474")

    response = client.get(url)
    assert response.status_code == 302

def test_get_login_with_fake_session():
    """
    Testing login page with fake user session
    Method : GET
    """
    server_name = app.config["SERVER_NAME"] or "localhost"
    client.set_cookie(server_name, 'token', "1111")
    response = client.get(url)
    assert response.status_code == 419

def test_post_login_with_wrong_data():
    """
    Testing login page with wrong data
    Method : POST
    """
    resp_dict = {"username":"user0011", "password":"fail"}
    response = client.post(url, data = resp_dict)
    assert response.location[-6:] == "/login"

def test_post_login_with_right_data():
    """
    Testing login page with right data
    Method : POST
    """
    resp_dict = {"username":"user0011", "password":"passofuser0011"}
    response = client.post(url, data = resp_dict)
    assert response.location[-1:] == "/"

def test_post_logout():
    """
    Testing logout page with right data
    Method : POST
    """
    set_token(client, "user9474")
    response = client.get('/login')

    url = '/logout'
    response = client.post(url, data = {})
    url = '/login'
    response = client.get(url)
    assert response.status_code == 200