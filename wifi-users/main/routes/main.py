from flask import Blueprint, render_template, flash, request, json
from main.extensions import db
from main.forms.filters import FilterForm

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def index():
    filters = FilterForm()
    # Load table's model
    connection_model = db.Table('Connection', db.metadata, autoload=True, autoload_with=db.engine)

    query = db.session.query(connection_model)  # Paginated query

    for key, value in request.args.to_dict().items():
        if key == 'username' and value != '':
            query = query.filter_by(connection_model.username.like("%" + value + "%"))
        if key == 'username_sum' and value != '':
            pass
        if key == 'datetime' and value != '':
            query = query.filter_by(connection_model.username.like(value))
        if key == 'ap_mac' and value != '':
            query = query.filter_by(connection_model.username.like(value))
        if key == 'client_mac' and value != '':
            query = query.filter_by(connection_model.username.like(value))

    connections = query.paginate(page=1, per_page=12)

    flash("Success!", "success")

    return render_template('main.html', connections=connections, filters=filters)
