from dotenv import load_dotenv
from main import create_app, db
import os

from main.services import insert_data_to_db

app = create_app()  # Creating Flask app instance
app.app_context().push()  # Loading app context

load_dotenv()  # Loading environment variables

if __name__ == '__main__':
    db.create_all()
    insert_data_to_db(db.engine)  # Creating database and insert
    app.run(debug=True, port=os.getenv('PORT'))
