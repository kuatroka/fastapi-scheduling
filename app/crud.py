from cassandra.cqlengine.management import sync_table
from .models import Product
from .db import get_session

session = get_session
sync_table(Product)


def create_entry(data: dict):
    return Product.create(**data)
