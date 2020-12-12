from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class FilterForm(FlaskForm):
    datetime = StringField('Datetime')
    ap_mac = StringField('AP MAC address')
    client_mac = StringField('Client MAC address')
    submit = SubmitField('Filter')

