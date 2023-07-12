from celery import Celery

import time

celery = Celery(backend="redis://localhost:6379/0", broker="amqp://guest@localhost:5672//")

@celery.task
def preprocessing_task(sleeping_time):
    print("OK")
    time.sleep(sleeping_time)
    return "ok"