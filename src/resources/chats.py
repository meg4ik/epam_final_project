from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request
from src import db
from src.database.models import Message, User

class Chats(Resource):
    @token_required
    def get(self):
        current_user = user_return()

        chats = db.session.query(Message).filter((Message.user_id_from == current_user.id) | (Message.user_id_to == current_user.id)).filter(Message.prev_message_id == None).all()

        users_chats = {}
        for i in chats:
            if i.user_id_from == current_user.id:
                user = db.session.query(User).filter_by(id = i.user_id_to).first()
                users_chats[user] = i
            else:
                user = db.session.query(User).filter_by(id = i.user_id_from).first()
                users_chats[user] = i

        return make_response(render_template("chats.html",auth=True, user=current_user,users_chats=users_chats),200)