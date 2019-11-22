from flask import Flask, request, Response, render_template
import requests
import itertools
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Regexp
import re

csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)

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
    


if (__name__ == "__main__"):
    app.run(debug=True)