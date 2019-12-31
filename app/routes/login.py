from flask import Blueprint, render_template, redirect
from flask_login import current_user, login_user
from app.forms.loginform import LogInForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.users import User

login_bp = Blueprint('login',__name__,template_folder='templates')

@login_bp.route('/login', methods=["POST","GET"])
def login():

    if(current_user.is_active):
        return "You are already logged in {}".format(current_user.username)

    form = LogInForm()
    messages = []
    if form.validate_on_submit():

        username = form.username_field.data

        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if(user != None and check_password_hash(user.password_hash,password)):
            login_user(user)
            return redirect('/index')
        else:
            messages.append("Invalid login attempt")
            return render_template('/login.html', form=form, messages=messages)
    else:
        return render_template('/login.html', form=form, messages=messages)
