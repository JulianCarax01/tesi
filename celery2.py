from celery import Celery

import time

celery = Celery(backend="redis://13.48.44.122:6379/0",
                broker="amqp://BlackMamba:Kobe@13.48.44.122:5672//")


@celery.task
def preprocessing_task(sleeping_time):
    print("OK")
    time.sleep(sleeping_time)
    return "ok"
