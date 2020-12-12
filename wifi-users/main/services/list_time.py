import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = os.getenv('DATA_PATH')


def list_times(engine, username):
    dataframe = pd.read_sql_table(table_name='Connection', con=engine)
    dataframe.reset_index(drop=True, inplace=True)


    dataframe = dataframe[dataframe.username == username]
    
    del dataframe['connection_id'], dataframe['username'], dataframe['index'], dataframe['start_time'], dataframe['stop_time'], dataframe['client_mac'], dataframe['input_octets'], dataframe['output_octets'], dataframe['ap_mac']
    

    dataframe.drop_duplicates(inplace=True)

    data_dict = dataframe.to_dict('list')

    times = data_dict['duration']

    return times
