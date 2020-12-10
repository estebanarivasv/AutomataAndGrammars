import os
from dotenv import load_dotenv
from flask import Flask

# Loading environment variables
load_dotenv()

def create_app():
    # Flask application instance
    app = Flask(__name__)

    return app
