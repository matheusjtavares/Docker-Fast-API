from typing import Union
from fastapi import FastAPI

from .db_helper import dbHelper

app = FastAPI()

@app.get("/test-connection")
def start_db_connection():
    dbHelper1 = dbHelper()
    return {"Hello": dbHelper1.status}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}