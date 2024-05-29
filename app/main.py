from typing import Union
from fastapi import FastAPI
import datetime as dt
from .modules.db_source_helper import dbSourceHelper
from fastapi import FastAPI, Request,HTTPException
from starlette.responses import RedirectResponse
from pydantic import BaseModel
import json

# the base model
class QueryParams(BaseModel):
    variables: str
    start_date: str
    end_date: str

app = FastAPI()

@app.post("/get-source-data")
def start_db_connection(query: QueryParams):
    variables = query.variables
    start_date = query.start_date
    end_date = query.end_date
    default_variables = ['wind_speed','power','ambient_temperature']
    try:
        start_date_dt = dt.datetime.strptime(start_date,"%Y-%m-%d %H:%M")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Wrong start date format, use %Y-%m-%d %H:%M")
    try:
        end_date_dt = dt.datetime.strptime(end_date,"%Y-%m-%d %H:%M")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Wrong end date format, use %Y-%m-%d %H:%M")
    variables_list = variables.split(',')
    variables_list = [x for x in variables_list if x in default_variables]
    if len(variables_list)==0:
        raise HTTPException(status_code=400 , detail="Choose one or more variables among variable from the following list: wind_speed,power or ambient_temperature. Use ',' for multiple variables")


    dbHelper = dbSourceHelper()
    query_df = dbHelper.get_input_data(variables_list,start_date=start_date_dt,end_date=end_date_dt)
    if not query_df.empty:
        query_df.ts = query_df.ts.dt.strftime("%Y-%m-%d %H:%M")
    print(query_df.head())
    return json.loads(query_df.to_json( orient='records'))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}