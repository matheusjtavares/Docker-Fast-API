from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os
from datetime import datetime as dt

load_dotenv(find_dotenv())

class dbSourceHelper():
    '''Class that connects to the source database. Use its functions to navigate ,or its engine to perform custom queries into it.'''
    def __init__(self):
        user = os.environ.get("POSTGRES_USER")
        password = os.environ.get("POSTGRES_PASSWORD")
        host = os.environ.get("POSTGRES_SOURCE_HOST")
        port = 5432 # Default PostgreSQL port is 5432
        database = os.environ.get("POSTGRES_SOURCE_DB")

        # Create the connection URL
        connection_url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

        # Create the SQLAlchemy engine
        self.engine = create_engine(connection_url)

        # Test the connection (optional)
        try:
            with self.engine.connect() as connection:
                print("Connection to PostgreSQL database successful")
                self.status =  "Connection to PostgreSQL database successful"
        except Exception as e:
            print(f"Error: {e}")
            self.status =  "Failed to PostgreSQL database successful"
            
    def get_input_data(self,columns:str,start_date:dt,end_date:dt):
        '''Gets all data within the data table'''
        if len(columns)==0:
            print('At least one column should be selected')
            raise Exception
        columns_clause = ' '.join([f'{column},' for column in columns])
        query = '''
        SELECT ''' + columns_clause + ''' 
            TS
            FROM DATA
            WHERE TS between %(start_date)s AND  %(end_date)s
        '''
        query_df = pd.read_sql(query,self.engine,params = {'start_date':start_date,'end_date':end_date})
        return query_df
    