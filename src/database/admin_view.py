import uuid

from flask import flash, redirect, url_for
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import generate_password_hash
from src.token import token_required, user_return


class AdminIndexView(AdminIndexView):
    """
    Flask-admin custom view
    Overrides AdminIndexView for main admin page
    """
    @token_required
    @expose('/')
    def index(self):
        """
        Return index admin page in flaks-admin session
        """

        #take current session user
        current_user = user_return()
        #if user statust admin calculate sum of user paychecks
        if current_user.is_admin:
            #return index page
            return super(AdminIndexView, self).index()
        else:
            #current session user status is not admin
            flash("No permission for this page",category='danger')
            return redirect(url_for('main'))

class UserModelView(ModelView):
    """
    Flask-admin custom view
    Overrides ModelView for User model repr
    """
    def create_form(self, obj=None):
        """
        Method overrides creating form for User model
        Adding custom uuid to uuid data in the entered field
        """
        form = super().create_form(obj=obj)
        new_uuid = str(uuid.uuid4())
        form.uuid.data = new_uuid
        #return form
        return form
    def on_model_change(self, form, model, is_created):
        """
        Method overrides updating form for User model
        Takes and set custom password and uuid
        Nothing to return
        """
        if is_created:
            model.password = generate_password_hash(form.password.data).decode('utf8')
        else:
            if form.password.data:
                model.password = generate_password_hash(form.password.data).decode('utf8')
        if not form.uuid.data:
                model.uuid = str(uuid.uuid4())

class DepartmentModelView(ModelView):
    """
    Flask-admin custom view
    Overrides ModelView for Department model repr
    """
    def create_form(self, obj=None):
        """
        Method overrides creating form for Department model
        Adding custom uuid to uuid data in the entered field
        """
        form = super().create_form(obj=obj)
        new_uuid = str(uuid.uuid4())
        form.uuid.data = new_uuid
        #return form
        return form
    def on_model_change(self, form, model, is_created):
        """
        Method overrides updating form for Department model
        Takes and set uuid
        Nothing to return
        """
        if not form.uuid.data:
                model.uuid = str(uuid.uuid4())
        