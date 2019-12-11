from flask import Flask, request, Response, render_template
from flask_login import login_user
from newstoryform import NewStoryForm, priority_levels, priority_levels_list
from werkzeug.security import generate_password_hash, check_password_hash

import requests

from app import app, db
from signupform import SignUpForm
from loginform import LogInForm
from models import User

import json

@app.route("/")
@app.route("/index")
def index():
    return render_template('/index.html')

@app.route('/login')
def login():

    form = LogInForm()
    if form.validate_on_submit():

        username = form.username_field.data

        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if(check_password_hash(password,user[1])):
            login_user(user)
        else:
            pass

    else:
        return render_template('/login.html')


@app.route('/signup')
def signup():

    form = SignUpForm()
    if form.validate_on_submit():

        username = form.username_field.data

        password = form.password.data

        u = User(username=username,password=generate_password_hash(password))

        db.session.add(u)
        db.session.commit()
        
    else:
        return render_template('/signup.html')

@app.route('/newstory', methods=['POST','GET'])
def newstory():

    form = NewStoryForm()
    if form.validate_on_submit():
        story_name = form.name_field.data.replace("'","")

        description = form.description_field.data.replace("'","")

        priority = int(form.priority_field.data)

        date = form.date_field.data
        
        return storyboard() #throw them to the storyboard
    else:
        return render_template('/newstory.html',form=form)
        
@app.route('/storyboard')
def storyboard():

    return render_template('/storyboard.html', stories=stories)


@app.route('/deletestory/<story_id>',methods=["POST","GET"])
def deletestory(story_id):
    
    print("Story {} deleted".format(story_id))
    
    return json.dumps({'succecss':True}),200,{'ContentType':'application/json'}

    

@app.route('/proxy')
def proxy():
    result = requests.get(request.args['url'])
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp