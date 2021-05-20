import src
from src import app

def test_main_route():
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200