import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = os.getenv('DATA_PATH')


def insert_data_to_db(db):
    dataframe = pd.read_csv(DATA_PATH, sep=';')
    try:
        dataframe.to_sql(name='Connection', con=db.engine, index=False)
    except ValueError:
        pass
