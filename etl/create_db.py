from sqlalchemy import create_engine
from sqlalchemy import text

import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
port = 5433 # Default PostgreSQL port is 5432
database = os.environ.get("POSTGRES_TARGET_DB")
# Create the connection URL
connection_url = f'postgresql+psycopg2://{user}:{password}@localhost:{port}/postgres'

# Create the SQLAlchemy engine
engine = create_engine(connection_url)
# Connect to the PostgreSQL server and create the new database
with engine.connect() as connection:
    connection = connection.execution_options(isolation_level="AUTOCOMMIT")
    connection.execute(text(f"CREATE IF NOT EXISTS DATABASE {database}"))
    print(f"Database '{database}' created successfully.")
