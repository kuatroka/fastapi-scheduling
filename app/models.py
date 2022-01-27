from operator import index
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

data = {"asin": "AMZNIDNUMBER3", "title": "Mark 1"}


class Product(Model):  # -> table
    __keyspace__ = "scraper_app"
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default="-1")


# this is a detailed view/table for asin
class ProductScrapeEvent(Model):  # -> table
    __keyspace__ = "scraper_app"
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index=True)
    title = columns.Text()
    price_str = columns.Text(default="-1")


# class ProductScrapeEvent(Model):  # -> table
#     __keyspace__ = "scraper_app"
#     uuid = columns.UUID(primary_key=True)
#     asin = columns.Text(index=True)
#     title = columns.Text()
#     price_str = columns.Text(default="-1")