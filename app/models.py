from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# data = {"asin": "AMZNIDNUMBER", "title": "Mark 1"}


class Product(Model):
    __keyspace__ = "scraper_app"
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default="-1")
