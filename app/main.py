from typing import Union
from fastapi import FastAPI
import datetime as dt
from .db_helper import dbHelper
import json
app = FastAPI()

@app.get("/test-connection")
def start_db_connection():
    start_date = dt.datetime(2024,5,1)
    end_date = dt.datetime(2024,5,5)
    dbHelper1 = dbHelper()
    query_df = dbHelper1.get_input_data(['wind_speed','power'],start_date=start_date,end_date=end_date)
    print(query_df.head())
    return json.loads(query_df.to_json( orient='records'))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}