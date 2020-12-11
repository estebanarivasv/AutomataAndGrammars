from flask import Blueprint, render_template, flash, request, json
import re

from main.extensions import db
from main.forms.filters import FilterForm
from main.models.connections import Connection as ConnectionModel

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
