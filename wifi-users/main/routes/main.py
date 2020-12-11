from flask import Blueprint, render_template, flash
from main.extensions import db
from main.forms.filters import FilterForm

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def index():
    filters = FilterForm()
    # Load table's model
    connection_model = db.Table('Connection', db.metadata, autoload=True, autoload_with=db.engine)

    connections = db.session.query(connection_model).paginate(page=1, per_page=12)  # Paginated query

    if filters.validate_on_submit():
        flash("Success")

    return render_template('main.html', connections=connections, filters=filters)
