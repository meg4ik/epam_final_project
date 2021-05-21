import src
from src import app, db
from src.database.models import User

from tests.tokens import set_token

from src.database.models import Message, User

client = app.test_client()


def test_get_chat_route_with_no_mess():
    """
    Testing chat page with no message between users
    Method : GET
    """
    user =  db.session.query(User).filter(User.username == "user5566").first()
    url = '/chat/{}'.format(user.uuid)
    set_token(client, "user8989")
    response = client.get(url)
    assert response.status_code == 200

def test_get_chat_route_with_mess():
    """
    Testing chat page with messages between users
    Method : GET
    """
    user1 =  db.session.query(User).filter(User.username == "user7433").first()
    user2 =  db.session.query(User).filter(User.username == "user0011").first()
    url = '/chat/{}'.format(user1.uuid)
    set_token(client, "user0011")

    mess = Message(
            user_id_from = user1.id,
            user_id_to=user2.id,
            prev_message_id=None,
            text="test"
        )
    db.session.add(mess)
    db.session.commit()
    
    response = client.get(url)
    db.session.delete(mess)

    db.session.commit()
    db.session.close()
    assert response.status_code == 200

def test_get_wrong_chat_route():
    """
    Testing chat page with wrong uuid
    Method : GET
    """
    url = '/chat/{}'.format("1111")
    set_token(client, "user0011")

    response = client.get(url)
    assert response.status_code == 302


def test_post_chat_route():
    """
    Testing chat page as adding new mess
    Method : POST
    """
    user_to =  db.session.query(User).filter(User.username == "user0011").first()
    url = '/chat/{}'.format(user_to.uuid)
    set_token(client, "user7433")
    
    response = client.post(url, data={"m":"text"})
    
    assert response.status_code == 302

def test_post_wrong_chat_route():
    """
    Testing chat page with wrong uuid
    Method : POST
    """
    url = '/chat/{}'.format("1111")
    set_token(client, "user0011")

    response = client.post(url)
    assert response.status_code == 302
