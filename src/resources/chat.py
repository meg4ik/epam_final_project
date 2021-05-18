from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request, flash, redirect, url_for
from src.database.models import User, Message
from src import db

def get_last_mess(curr_id, to_id):
    """
    return message obj that first in curr_id to to_id users chat
    """
    return db.session.query(Message).filter(((Message.user_id_from == curr_id) & (Message.user_id_to == to_id)) | (
            (Message.user_id_from == to_id) & (Message.user_id_to == curr_id))).filter(Message.prev_message_id == None).first()

class Chat(Resource):
    """
    Chat resource
    Сontains messages in current chat
    Requires uuid user as uuid_to
    Authentication is required
    """
    @token_required
    def get(self, uuid_to=None):
        """
        Get method
        Return "chat.html" with auth flag, list of messages, current user obj
        In case of exception can return main page
        """

        # get user obj bu uuid in link
        user_obj_to = db.session.query(User).filter_by(uuid=uuid_to).first()
        if not uuid_to or not user_obj_to:
            #return main.html
            flash("Not such a user", category='danger')
            return redirect(url_for('main'))
        #take current session user
        current_user = user_return()
        mess_dict = []
        #get firts message form chat chain
        first_mes = get_last_mess(current_user.id, user_obj_to.id)
        #return chat page with no message if first message was not found
        if not first_mes:
            return make_response(render_template("chat.html", auth=True, user=current_user, mess_dict=mess_dict), 200)
        next_mess_id = first_mes.id
        #add first message in list
        mess_dict.append([first_mes.user_from,first_mes.text])
        #adding all message in cycle
        while True:
            next_mess = db.session.query(
                Message).filter_by(prev_message_id=next_mess_id).first()
            if not next_mess:
                break
            else:
                mess_dict.append([next_mess.user_from, next_mess.text])
                next_mess_id = next_mess.id
        #return chat.html with list of messages
        return make_response(render_template("chat.html", auth=True, user=current_user, mess_dict=mess_dict), 200)
    
    @token_required
    def post(self, uuid_to=None):
        """
        Post method
        Return redirect to "chat.html" with user uuid
        In case of exception can return main page
        """

        #take current session user
        current_user = user_return()
        #get user obj bu uuid in link
        user_obj_to = db.session.query(User).filter_by(uuid = uuid_to).first()
        if not uuid_to or not user_obj_to:
            #return main.html
            flash("Not such a user", category='danger')
            return redirect(url_for('main'))
        #get firts message form chat chain
        first_mes = get_last_mess(current_user.id, user_obj_to.id)
        #get last message id in user-to-user chat
        if not first_mes:
            next_mess_id = None
        else:
            next_mess_id = first_mes.id
            while True:
                next_mess = db.session.query(
                    Message).filter_by(prev_message_id=next_mess_id).first()
                if not next_mess:
                    break
                else:
                    next_mess_id = next_mess.id
        m = request.form.get('m')
        #create message object
        mess = Message(
            user_id_from = current_user.id,
            user_id_to=user_obj_to.id,
            prev_message_id=next_mess_id,
            text=m
        )
        db.session.add(mess)
        db.session.commit()
        db.session.close()
        #return redirect to chat with user uuid
        return redirect(url_for('chat', uuid_to = uuid_to))
