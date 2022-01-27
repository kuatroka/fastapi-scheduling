from fastapi import FastAPI
from . import (config, db, models)
from cassandra.cqlengine.management import sync_table

settings = config.get_settings()

app = FastAPI()

session = None

app.on_event("startup")


def on_startup():

    global session
    session = db.get_session()
    sync_table(models.Product)
    sync_table(models.ProductScrapeEvent)


@app.get("/")
def read_index():
    return {"hello": "new world order", "proj_name": settings.proj_name}