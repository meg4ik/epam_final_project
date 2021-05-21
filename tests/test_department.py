import src
from src import app, db
from src.database.models import Department

from tests.tokens import set_token

client = app.test_client()

def test_get_department_route():
    """
    Testing department page
    Method : GET
    """
    user =  db.session.query(Department).filter(Department.title == "Bank blockchain").first()
    url = '/department/{}'.format(user.uuid)
    set_token(client, "user0011")

    response = client.get(url)
    assert response.status_code == 200

def test_get_wrong_department_route():
    """
    Testing department page with wrong uuid
    Method : GET
    """
    url = '/department/{}'.format("1111")
    set_token(client, "user0011")

    response = client.get(url)
    assert response.status_code == 302
