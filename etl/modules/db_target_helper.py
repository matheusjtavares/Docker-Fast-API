from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class dbTargetHelper():
    '''Class that connects to the target database. Use its functions to navigate ,or its engine to perform custom queries into it.'''
    def __init__(self):
        user = os.environ.get("POSTGRES_USER")
        password = os.environ.get("POSTGRES_PASSWORD")
        host = os.environ.get("POSTGRES_TARGET_HOST")
        port = 5432 # Default PostgreSQL port is 5432
        database = os.environ.get("POSTGRES_TARGET_DB")
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
            
    def get_aggregation_methods(self)->pd.DataFrame:
        '''Gets all mapped aggregation methods from the database'''
        query = '''SELECT * FROM aggregation'''
        df = pd.read_sql(query,self.engine)
        return df
    
    def get_signals(self)->pd.DataFrame:
        '''Gets all mapped signals from the database'''
        query = '''SELECT * FROM signal'''
        df = pd.read_sql(query,self.engine)
        return df
    