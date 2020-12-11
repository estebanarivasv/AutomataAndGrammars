from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Regexp


class FilterForm(FlaskForm):
    datetime = StringField('Datetime', validators=[
        Regexp('\d\d/\d\d/\d\d\d\d \d\d:\d\d', message="Date must be in this format DD/MM/YYYY HH:MM")
    ])
    ap_mac = StringField('AP MAC address', validators=[
        Regexp('(?:[0-9a-fA-F]{2}\-){5}[0-9a-fA-F]{2}(:UM)?', message="AP MAC address must be in this format 04-18-D6-22-94-E7:UM")
    ])
    client_mac = StringField('Client MAC address', validators=[
        Regexp('(?:[0-9a-fA-F]{2}\-){5}[0-9a-fA-F]{2}(:UM)?', message="Client MAC address must be in this format 04-18-D6-22-94-E7")
    ])
    submit = SubmitField('Filter')

