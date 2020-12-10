import os
from dotenv import load_dotenv
from flask import Flask

from main.extensions import db

# Loading environment variables
load_dotenv()

DB_PATH = os.getenv('DB_PATH')
DB_NAME = os.getenv('DB_NAME')
DB_URI = "sqlite:////" + DB_PATH + DB_NAME


def create_app():
    # Flask application instance
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    return app
