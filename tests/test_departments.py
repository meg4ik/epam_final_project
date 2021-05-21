import src
from src import app

from tests.tokens import set_token

client = app.test_client()
url = '/departments/1'

def test_get_user_route_auth_not_admin():
    """
    Testing departments page
    Method : GET
    """
    set_token(client, "user0011")

    response = client.get(url)
    assert response.status_code == 200