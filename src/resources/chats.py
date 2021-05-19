from flask import make_response, render_template
from flask_restful import Resource
from src import db
from src.database.models import Message, User
from src.token import token_required, user_return


class Chats(Resource):
    """
    Chat resource
    Сontains chats which belong to the user
    Authentication is required
    """
    @token_required
    def get(self):
        """
        Get method
        Return "chats.html" with auth flag, list of messages, current user obj
        In case of exception can return main page
        """

        #take current session user
        current_user = user_return()
        #get all current user chats
        chats = db.session.query(Message).filter((Message.user_id_from == current_user.id) | (Message.user_id_to == current_user.id)).filter(Message.prev_message_id == None).all()
        #make dictionary with user obj and message data
        users_chats = {}
        for i in chats:
            if i.user_id_from == current_user.id:
                user = db.session.query(User).filter_by(id = i.user_id_to).first()
                users_chats[user] = i
            else:
                user = db.session.query(User).filter_by(id = i.user_id_from).first()
                users_chats[user] = i
        #return chats.html with auth flag, user from session and dict with chats
        return make_response(render_template("chats.html",auth=True, user=current_user,users_chats=users_chats),200)
