from celery import Celery
from celery.signals import worker_process_init, beat_init
from . import config, db, models
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

celery_app = Celery(__name__)
settings = config.get_settings()

REDIS_URL = settings.redis_url
celery_app.conf.broker_url = REDIS_URL
celery_app.conf.result_backend = REDIS_URL

Procuct = models.Product
ProductScrapeEvent = models.ProductScrapeEvent


def celery_on_startup(*args, **kwargs):
    print("hello world")
    if connection.session is not None:
        connection.cluster.shutdown()
    if connection.session is not None:
        connection.cluster.shutdown()

    cluster = db.get_cluster()
    session = cluster.connect()
    connection.register_connection(str(session), session=session)
    connection.set_default_connection(str(session))
    sync_table(Procuct)
    sync_table(ProductScrapeEvent)


beat_init.connect(celery_on_startup)
worker_process_init.connect(celery_on_startup)


@celery_app.task
def random_task(name):
    print(f"Who throws the shoe. Honestly {name}")


@celery_app.task
def list_products():
    q = Procuct.objects.all().values_list("asin", flat=True)
    print(list(q))