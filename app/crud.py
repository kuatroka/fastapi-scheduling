import uuid
from cassandra.cqlengine.management import sync_table
from .models import Product, ProductScrapeEvent
from .db import get_session

session = get_session
sync_table(Product)
sync_table(ProductScrapeEvent)


def create_entry(data: dict):
    return Product.create(**data)


def create_scrape_entry(data: dict):
    data["uuid"] = uuid.uuid1()  # includes timestamp
    return ProductScrapeEvent.create(**data)


def add_scrape_event(data: dict):
    product = create_entry(data)
    scrape_obj = create_scrape_entry(data)

    return product, scrape_obj


data = {"asin": "AMZNIDNUMBER", "title": "Mark 1"}

# ProductScrapeEvent = models.ProductScrapeEvent()
create_scrape_entry(data)
