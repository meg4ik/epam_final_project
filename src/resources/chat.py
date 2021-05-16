import uuid
from flask_restful import Resource
from src.token import token_required, user_return
from flask import make_response, render_template, request, flash, redirect, url_for
from src.database.models import User, Message
from src import db

def get_last_mess(curr_id, to_id):
    return db.session.query(Message).filter(((Message.user_id_from == curr_id) & (Message.user_id_to == to_id)) | (
            (Message.user_id_from == to_id) & (Message.user_id_to == curr_id))).filter(Message.prev_message_id == None).first()

class Chat(Resource):
    @token_required
    def get(self, uuid_to=None):
        user_obj_to = db.session.query(User).filter_by(uuid=uuid_to).first()
        if not uuid_to or not user_obj_to:
            flash("Not such a user", category='danger')
            return redirect(url_for('main'))
        current_user = user_return()
        mess_dict = {}
        first_mes = get_last_mess(current_user.id, user_obj_to.id)
        if not first_mes:
            return make_response(render_template("chat.html", auth=True, user=current_user, mess_dict=mess_dict), 200)
        next_mess_id = first_mes.id
        mess_dict[first_mes.user_from.uuid] = first_mes.text
        while True:
            next_mess = db.session.query(
                Message).filter_by(prev_message_id=next_mess_id).first()
            if not next_mess:
                break
            else:
                mess_dict[next_mess.user_from.uuid] = next_mess.text
                next_mess_id = next_mess.id
        return make_response(render_template("chat.html", auth=True, user=current_user, mess_dict=mess_dict), 200)
    
    @token_required
    def post(self, uuid_to=None):
        current_user = user_return()
        user_obj_to = db.session.query(User).filter_by(uuid = uuid_to).first()
        if not uuid_to or not user_obj_to:
            flash("Not such a user", category='danger')
            return redirect(url_for('main'))

        first_mes = get_last_mess(current_user.id, user_obj_to.id)
        next_mess_id = first_mes.id
        while True:
            next_mess = db.session.query(
                Message).filter_by(prev_message_id=next_mess_id).first()
            if not next_mess:
                break
            else:
                next_mess_id = next_mess.id
        m = request.form.get('m')
        mess = Message(
            user_id_from = current_user.id,
            user_id_to=user_obj_to.id,
            prev_message_id=next_mess_id,
            text=m
        )
        db.session.add(mess)
        db.session.commit()
        db.session.close()
        return redirect(url_for('chat', uuid_to = uuid_to))
