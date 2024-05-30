from sqlalchemy import create_engine
from modules.db_target_helper import dbTargetHelper
from sqlalchemy import text
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Float,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv,find_dotenv
import time

load_dotenv(find_dotenv())

user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
host = os.environ.get("POSTGRES_TARGET_HOST")
port = 5432 # Default PostgreSQL port is 5432
database = os.environ.get("POSTGRES_TARGET_DB")
# Create the connection URL
connection_url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/postgres'
# Create the SQLAlchemy engine
engine = create_engine(connection_url)

# Test the connection (optional)
try:
    with engine.connect() as connection:
        print("Connection to PostgreSQL database successful")
except Exception as e:
    print(f"Error: {e}")


with engine.connect() as connection:
    connection = connection.execution_options(isolation_level="AUTOCOMMIT")
    connection.execute(text(f"CREATE DATABASE {database}"))
    print(f"Database '{database}' created successfully.")

dbHelper = dbTargetHelper()

engine = dbHelper.engine


# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Define the base class
Base = declarative_base()

# Define the table schema
class signalTable(Base):
    __tablename__ = 'signal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
# Define the table schema
class aggregationTable(Base):
    __tablename__ = 'aggregation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class dataTable(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ts = Column(DateTime, nullable=False)
    signal_id = Column(Integer, ForeignKey('signal.id'), nullable=False)
    agg_id = Column(Integer, ForeignKey('aggregation.id'), nullable=False)
    value = Column(Float, nullable=False)

# Create all tables in the database
Base.metadata.create_all(engine)

print("Tables 'signal', 'aggregation', 'data' created successfully.")
# Add REcords
for signal in ['wind_speed','power','ambient_temperature']:
    new_signal = signalTable(name=signal)
    session.add(new_signal)
    session.commit()

for aggregation in ['mean','min','max','std']:
    new_agg = aggregationTable(name=aggregation)
    session.add(new_agg)
    session.commit()

connection = engine.connect()
print('Registers added to target')