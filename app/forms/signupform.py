from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField


class SignUpForm(FlaskForm):

    username_field = StringField(u"Username: ")

    password = PasswordField(u"Password: ")

    confirm_password = PasswordField(u"Confirm Password: ")
    
    team_name = StringField(u"Team name: ")

    team_password = PasswordField(u"Team password: ")

    team_password_cofirm = PasswordField(u"Confirm team password: ")

    submit = SubmitField(u"Create")