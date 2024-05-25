from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv('../.env')
class dbHelper():
    def __init__(self):
        user = 'postgres'
        password = 'postgres'
        host = 'postgreshost'
        port = 5432 # Default PostgreSQL port is 5432
        database = 'postgres_prova'

        # Create the connection URL
        connection_url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

        # Create the SQLAlchemy engine
        engine = create_engine(connection_url)

        # Test the connection (optional)
        try:
            with engine.connect() as connection:
                print("Connection to PostgreSQL database successful")
                self.status =  "Connection to PostgreSQL database successful"
        except Exception as e:
            print(f"Error: {e}")
            self.status =  "Failed to PostgreSQL database successful"

    