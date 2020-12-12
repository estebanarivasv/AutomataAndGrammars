from platform import mac_ver
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = os.getenv('DATA_PATH')


def list_mac_addresses(engine, username):
    dataframe = pd.read_sql_table(table_name='Connection', con=engine)
    dataframe.reset_index(drop=True, inplace=True)


    dataframe = dataframe[dataframe.username == username]
    
    del dataframe['connection_id'], dataframe['username'], dataframe['index'], dataframe['start_time'], dataframe['stop_time'], dataframe['duration'], dataframe['input_octets'], dataframe['output_octets'], dataframe['ap_mac']
    

    dataframe.drop_duplicates(inplace=True)

    data_dict = dataframe.to_dict('list')

    mac_addresses = data_dict['client_mac']

    return mac_addresses
