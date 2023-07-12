from celery import Celery

import time

celery = Celery(backend="redis://16.171.146.217:6379/0", broker="amqp://BlackMamba:Kobe@16.171.146.217:5672//")


@celery.task
def preprocessing_task(sleeping_time):
    print("OK")
    time.sleep(sleeping_time)
    return "ok"


