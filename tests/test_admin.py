import src
from src import app, db

from tests.tokens import set_token


client = app.test_client()


def test_get_admin_route_auth_not_admin():
    """
    Testing chat page with not admin user session
    Method : GET
    """

    url = '/admin/'
    set_token(client, "user0011")
    response = client.get(url)
    assert response.status_code == 302

def test_get_admin_route_auth_admin():
    """
    Testing chat page with admin user session
    Method : GET
    """

    url = '/admin/'
    set_token(client, "user9474")
    response = client.get(url)
    assert response.status_code == 200