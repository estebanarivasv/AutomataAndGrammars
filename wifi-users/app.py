from dotenv import load_dotenv
from main import create_app
import os
import time

from main.services import insert_data_to_db

app = create_app()                  # Creating Flask app instance
app.app_context().push()            # Loading app context

load_dotenv()                       # Loading environment variables

DB_PATH = os.getenv('DB_PATH')
DB_NAME = os.getenv('DB_NAME')


if __name__ == '__main__':
    # If the database doesn't exist, we show a warning
    if not os.path.exists(DB_PATH + DB_NAME):
        print('WARNING: Database is not created!')
        insert_data_to_db()
    time.sleep(5)
    app.run(debug=True, port=os.getenv('PORT'))
