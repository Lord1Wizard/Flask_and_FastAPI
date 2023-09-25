import logging
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()


@app.get('/')
async def root():
    logger.info('Отработал GET запрос')
    return {"message":"Hello World"}


# @app.get('/items/{item_id}')
# async def read_item(item_id: int, q: str =None):
#     return {"item_id": item_id, "q": q}

@app.post('/items/')
async def create_item(item: Item):
    logger.info('Отработал POST запрос')
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id ={item_id}.')
    return {"item_id": item_id}

@app.get("/index/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"
