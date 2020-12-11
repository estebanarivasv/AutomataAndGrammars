from flask import Blueprint, render_template, flash, request, json
from main.extensions import db
from main.forms.filters import FilterForm

from main.models.connections import Connection as ConnectionModel
main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def index():
    page=1
    filters = FilterForm()

    query = db.session.query(ConnectionModel)

    for key, value in request.args.to_dict().items():
        if key == 'datetime' and value != '':
            query = query.filter(ConnectionModel.start_time.like(value))
        if key == 'ap_mac' and value != '':
            query = query.filter(ConnectionModel.ap_mac.like(value))
        if key == 'client_mac' and value != '':
            query = query.filter(ConnectionModel.client_mac.like(value))

        if key == 'page_num' and value != '':
            page = int(value)

    connections = query.paginate(page=page, per_page=12)        # Paginated query

    flash("Success!", "success")

    return render_template('main.html', connections=connections, filters=filters)
