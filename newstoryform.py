from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField
from wtforms import validators
from wtforms.fields.html5 import EmailField


priority_levels = [(0,"High"),(1,"Medium"),(2,"Low")]
priority_levels_list = ["High","Medium","Low"]

class NewStoryForm(FlaskForm):

    name_field = StringField(u"Story Name: ")

    priority_field = SelectField(u"Priority: ",choices=priority_levels,coerce=int)

    description_field = TextAreaField(u'Description: ')

    date_field = DateField(u'Due Date: ',format='%m-%d-%Y', render_kw={"placeholder": 'mm-dd-yyyy'})

    email = EmailField('Email Address: ', [validators.Email()])

    submit = SubmitField(u'Create')
