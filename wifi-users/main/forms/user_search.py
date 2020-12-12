from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    username = StringField('Username')
    search = SubmitField('Search')

