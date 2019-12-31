from flask import Blueprint, redirect, render_template
from flask_login import current_user, login_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

import sqlite3

from app.utils import *
from app.config import Config
from app.models.users import User
from app.forms.signupform import SignUpForm

signup_bp = Blueprint('signup',__name__, template_folder='templates')

@signup_bp.route('/signup', methods=["POST","GET"])
def signup():

    form = SignUpForm()
    messages = []
    if form.validate_on_submit():

        #user stuff
        username = str(form.username_field.data)

        password = str(form.password.data)

        confirm_password = str(form.confirm_password.data)

        if(confirm_password != password):
            messages.append('User passwords do not match')


        #team stuff
        teamname = str(form.team_name.data)

        team_password = str(form.team_password.data)

        #this will not be "" if we are trying to make a team
        team_password_confirm = str(form.team_password_cofirm.data)

        making_new_team = (team_password_confirm is not "")

        #if we are making a new team and the passwords dont match
        if((team_password_confirm != team_password) and making_new_team):
            messages.append('Team passwords do not match')

        if(messages == []): #if there are no errors to this point


            conn = sqlite3.connect(Config.DATABASE_FILENAME)
            cursor = conn.cursor()

            if(making_new_team):
                try:
                    resp = cursor.execute(make_new_team_query_generator(teamname))
                    resp.fetchall()
                except sqlite3.OperationalError as e:
                    messages.append("Team name: '{}' is already taken".format(teamname))
                


                if(len(messages) == 0):
                    #shouldnt need to try/catch anything here because there should be
                    # a 1:1 for entries of teamnames and team tables
                    try:
                        query = place_new_team_into_teams(teamname,team_password)
                        resp = cursor.execute(query)
                        resp.fetchall()
                        conn.commit()
                    except sqlite3.OperationalError as e:
                        resp = cursor.execute("DROP TABLE {}".format(teamname))
                        resp.fetchall()
                        messages.append("Team name: '{}' is already taken".format(teamname))
                
            else: #if we are trying to join a team
                resp = cursor.execute("SELECT name,password_hash FROM teams WHERE name == '{}'".format(teamname))
                resp = resp.fetchall()
                if(len(resp) < 1 or check_password_hash(resp[0][1],team_password)):
                    messages.append("Team password invalid")
        
        if(len(messages) > 0):
            return render_template('/signup.html', form=form,messages=messages)
        else:
            resp = cursor.execute(place_new_user_gererator(username,password,teamname))
            resp = resp.fetchall()
            conn.commit()

            user = User.query.filter_by(username=username).first()
            if(check_password_hash(user.password_hash,password)):
                login_user(user)
            else:
                return "There was a problem signing you in..."

            return redirect('/index')
    else:
        return render_template('/signup.html', form=form,messages=messages)
