from typing import Union
from webbrowser import get

from fastapi import FastAPI

from db.db import get_connection

app = FastAPI()


@app.get("/")
def read_root():
    s = get_connection("zzz")
    return {"Hello": str(s)}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}