import src
from src import app

from tests.tokens import set_token

client = app.test_client()
url = '/chats'

def test_get_chats_route():
    """
    Testing chats page
    Method : GET
    """
    set_token(client, "user0011")
    response = client.get(url)
    assert response.status_code == 200