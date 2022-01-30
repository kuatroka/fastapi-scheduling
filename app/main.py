from typing import List
from fastapi import FastAPI
from . import (config, db, models, schemas)
from cassandra.cqlengine.management import sync_table

settings = config.get_settings()
Product = models.Product
ProductScrapeEvent = models.ProductScrapeEvent

app = FastAPI()

session = None

app.on_event("startup")


def on_startup():

    global session
    session = db.get_session()
    sync_table(Product)
    sync_table(ProductScrapeEvent)


@app.get("/")
def read_index():
    return {"hello": "new world order", "proj_name": settings.proj_name}


@app.get("/products", response_model=List[schemas.ProductListSchema])
def products_list_view():
    return list(Product.objects.all())


@app.get("/products/{asin}")
def products_detail_view(asin):
    data = dict(Product.objects.get(asin=asin))
    events = list(ProductScrapeEvent.objects().filter(asin=asin))
    events = [
        schemas.schemas.ProductScrapeEventDetailSchema(**x) for x in events
    ]
    data["events"] = events
    return data