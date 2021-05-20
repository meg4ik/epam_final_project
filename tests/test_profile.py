import src
from src import app

from tests.tokens import set_token

client = app.test_client()
url = '/profile'

def test_get_profile_route_auth_not_admin():
    """
    Testing profile page with user session as not admin
    Method : GET
    """
    set_token(client, "user0011")

    response = client.get(url)
    assert response.status_code == 200

def test_get_profile_route_auth_admin():
    """
    Testing profile page with user session as admin
    Method : GET
    """
    set_token(client, "user9474")

    response = client.get(url)
    assert response.status_code == 200