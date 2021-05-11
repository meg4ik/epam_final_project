from operator import mod
from flask_admin import AdminIndexView
from flask_admin import expose
from src.token import token_required, user_return
from flask import flash, redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import generate_password_hash
import uuid

class AdminIndexView(AdminIndexView):
    @token_required
    @expose('/')
    def index(self):
        current_user = user_return()
        if current_user.is_admin:
            return super(AdminIndexView, self).index()
        else:
            flash("No permission for this page",category='danger')
            return redirect(url_for('main'))

class UserModelView(ModelView):
    def create_form(self, obj=None):
        form = super().create_form(obj=obj)
        new_uuid = str(uuid.uuid4())
        form.uuid.data = new_uuid
        return form
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.password = generate_password_hash(form.password.data).decode('utf8')
        else:
            if form.password.data:
                model.password = generate_password_hash(form.password.data).decode('utf8')
        if not form.uuid.data:
                model.uuid = str(uuid.uuid4())

class DepartmentModelView(ModelView):
    def create_form(self, obj=None):
        form = super().create_form(obj=obj)
        new_uuid = str(uuid.uuid4())
        form.uuid.data = new_uuid
        return form
    def on_model_change(self, form, model, is_created):
        if not form.uuid.data:
                model.uuid = str(uuid.uuid4())
        