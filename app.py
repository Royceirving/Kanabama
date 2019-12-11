import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/app')
sys.path.append(os.getcwd()+'templates/')

from config import Config
from flask import Flask, request, Response, render_template, flash, abort, redirect, url_for
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect

import json
import requests
import sqlite3

from signupform import SignUpForm
from loginform import LogInForm
from newstoryform import NewStoryForm, priority_levels, priority_levels_list
from utils import *

DATABASE_FILENAME = 'app.db'

csrf = CSRFProtect()
app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "Row the Boat"
csrf.init_app(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)



@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template('/index.html', current_user=current_user)

@app.route('/login', methods=["POST","GET"])
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
            flash("Logged in successfully")
            return index()
        else:
            messages.append("Invalid login attempt")
            return render_template('/login.html', form=form, messages=messages)
    else:
        return render_template('/login.html', form=form, messages=messages)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    if(current_user.is_active):
        message = "Error logging out! Please try again."
    else:
        message = "Log out successful"
    return render_template('/logout.html',message=message)

@app.route('/signup', methods=["POST","GET"])
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


            conn = sqlite3.connect(DATABASE_FILENAME)
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
                if(check_password_hash(resp[0][1],team_password)):
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

            return index()
    else:
        return render_template('/signup.html', form=form,messages=messages)

@app.route('/newstory', methods=['POST','GET'])
def newstory():

    form = NewStoryForm()
    if form.validate_on_submit():
        story_name = form.name_field.data.replace("'","")

        description = form.description_field.data.replace("'","")

        priority = int(form.priority_field.data)

        date = form.date_field.data

        state = 0

        conn = sqlite3.connect(DATABASE_FILENAME)
        cursor = conn.cursor()

        cursor.execute(commit_story_generator(
            current_user.teamname, story_name, description,
            priority, date, state
        ))
        conn.commit()
        
        return storyboard() #throw them to the storyboard
    else:
        return render_template('/newstory.html',form=form)
        
@app.route('/storyboard')
def storyboard():

    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    resp = cursor.execute(get_stories_for_team(current_user.teamname))
    stories = resp.fetchall()
    return render_template('/storyboard.html', stories=stories)


@app.route('/deletestory/<story_id>',methods=["POST","GET"])
def deletestory(story_id):
    try:

        conn = sqlite3.connect(DATABASE_FILENAME)
        cursor = conn.cursor()

        query = delete_story_in_team_generator(current_user.teamname,story_id)
        resp = cursor.execute(query)
        resp = resp.fetchall()
        conn.commit()
        return json.dumps({'succecss':True}),200,{'ContentType':'application/json'}
    except BaseException:
        return json.dumps({'fail':False}),500,{'ContentType':'application/json'}
        

    

@app.route('/proxy')
def proxy():
    result = requests.get(request.args['url'])
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp


#Model for users
class User(db.Model,UserMixin):

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    teamname = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User {} on team {}>'.format(self.username,self.teamname)    

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



if (__name__ == "__main__"):
    app.run(debug=True)