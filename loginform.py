from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  PasswordField


class LogInForm(FlaskForm):

    username_field = StringField(u"Username: ")

    password = PasswordField(u"Password")

    submit = SubmitField(u"Log In")