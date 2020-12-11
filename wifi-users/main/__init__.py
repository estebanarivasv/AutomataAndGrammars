import os
from dotenv import load_dotenv
from flask import Flask

from main.extensions import db
from main.routes.main import main as main_blueprint

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

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    db.init_app(app)

    #Verifica si la conexion es sqlite
    if os.getenv('SQLALCHEMY_DATABASE_TYPE') == 'sqlite':
        def activatePrimaryKeys(conection, conection_record):
            #Ejecuta el comando que activa claves foraneas en sqlite
            conection.execute('pragma foreign_keys=ON')

        with app.app_context():
            db.create_all()
            from sqlalchemy import event
            #Al conectar a la base de datos llamar a la función que activa la claves foraneas
            event.listen(db.engine, 'connect', activatePrimaryKeys)


    app.register_blueprint(main_blueprint)

    return app
