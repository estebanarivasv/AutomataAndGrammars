from flask import Blueprint, render_template, flash, request, jsonify, json
import re

from main.extensions import db
from main.forms import FilterForm, SearchForm
from main.models.connections import Connection as ConnectionModel
from main.services import list_mac_addresses, list_times

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def index():
    page = 1
    filters = FilterForm()

    query = db.session.query(ConnectionModel)

    for key, value in request.args.to_dict().items():
        if key == 'datetime' and value != '':
            matches = re.search(pattern='\d\d/\d\d/\d\d\d\d \d\d:\d\d', string=value)
            if not matches:
                flash("Date must be in this format DD/MM/YYYY HH:MM", "danger")
            else:
                query = query.filter(ConnectionModel.start_time.like(value))
        if key == 'ap_mac' and value != '':
            matches = re.search(pattern='(?:[0-9a-fA-F]{2}\-){5}[0-9a-fA-F]{2}(:UM)?', string=value)
            if not matches:
                flash("AP MAC address must be in this format 04-18-D6-22-94-E7:UM", "danger")
            else:
                query = query.filter(ConnectionModel.ap_mac.like(value))
        if key == 'client_mac' and value != '':
            matches = re.search(pattern='(?:[0-9a-fA-F]{2}\-){5}[0-9a-fA-F]{2}(:UM)?', string=value)
            if not matches:
                flash("Client MAC address must be in this format 04-18-D6-22-94-E7", "danger")
            else:
                query = query.filter(ConnectionModel.client_mac.like(value))

        if key == 'page_num' and value != '':
            page = int(value)

    connections = query.paginate(page=page, per_page=12)  # Paginated query

    return render_template('main.html', connections=connections, filters=filters)


@main.route('/users-mac', methods=["POST", "GET"])
def users_mac():
    mac_addresses = None
    form = SearchForm()

    if form.is_submitted():
        if form.username.data != '':
            mac_addresses = list_mac_addresses(db.engine, username=form.username.data)

    return render_template('users-mac.html', mac_addresses=mac_addresses, form=form)

@main.route('/users-time', methods=["POST", "GET"])
def users_time():
    times = None
    form = SearchForm()
    seconds = 0.0
    minutes = 0.0
    hours = 0.0
    days = 0.0

    if form.is_submitted():
        if form.username.data != '':
            times = list_times(db.engine, username=form.username.data)

            for time in times:
                seconds += time
                minutes = seconds / 60
                hours = minutes / 60
                days = hours / 24

    return render_template('users-time.html', seconds=seconds, minutes=minutes, hours=hours, days=days,form=form)