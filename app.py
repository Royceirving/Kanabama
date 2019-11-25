from flask import Flask, request, Response, render_template
import requests
import itertools
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import Regexp
import re

csrf = CSRFProtect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "row the boat"
csrf.init_app(app)

priority_levels = [(0,"High"),(1,"Medium"),(2,"Low")]

class NewStoryForm(FlaskForm):

    #TODO: Add validator for a story name
    name_field = StringField(u"Story Name: ")
    
    priority_field = SelectField(u"Priority: ",choices=priority_levels,coerce=int)

    description_field = TextAreaField(u'Description: ')
    
    date_field = DateField(u'Due Date: ',format='%m-%d-%Y')

    submit = SubmitField(u'Create')

@app.route("/")
@app.route("/index")
def index():
    return render_template('/index.html')

@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/signup')
def signup():
    return render_template('/signup.html')

@app.route('/newstory', methods=['POST','GET'])
def newstory():

    form = NewStoryForm()
    if form.validate_on_submit():
        story_name = form.name_field.data

        description = form.description_field.data

        priority = form.priority_field.data

        date = form.date_field.data;
        print(date)
        return render_template('/storyboard.html')
    else:
        return render_template('/newstory.html',form=form)
        
@app.route('/storyboard')
def storyboard():
    return render_template('/storyboard.html')

    

@app.route('/proxy')
def proxy():
    result = requests.get(request.args['url'])
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp

if (__name__ == "__main__"):
    app.run(debug=True)