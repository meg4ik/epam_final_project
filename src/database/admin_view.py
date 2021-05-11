from flask_admin import AdminIndexView
from flask_admin import expose
from src.token import token_required, user_return
from flask import flash, redirect, url_for

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
