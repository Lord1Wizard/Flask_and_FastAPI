import logging
from fastapi import FastAPI

from ..sem.task_01 import app1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.mount("/task_01/", app1)


@app.get('/')
async def root():
    logger.info('Отработал GET запрос')
    return {"message": "Hello World"}
