from typing import Union
from webbrowser import get
import hashlib
from fastapi import FastAPI

from db.db import get_connection

app = FastAPI()


@app.get("/")
def get():
    return {"msg": "hello stranger"}

@app.post("/")
def post_url(q: Union[str, None] = None):
    if q:
        hashed_string = hashlib.sha256(q.encode('utf-8')).hexdigest()[0:5]
        conn, node = get_connection(q)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO url_store(url, short_url) VALUES('{q}', '{hashed_string}')")
        conn.commit()
        return {"value": "q", "node": node['name']}
    return {"msg": "insert something mother fucker"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}