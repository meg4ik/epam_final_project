import src
from src import app

from tests.tokens import set_token

client = app.test_client()
url = '/about'

def test_get_about_route():
    """
    Testing about page with no session
    Method : GET
    """
    response = client.get(url)
    assert response.status_code == 200

def test_get_about_route_auth():
    """
    Testing about page with user session
    Method : GET
    """
    set_token(client, "user0011")

    response = client.get(url)
    assert response.status_code == 202