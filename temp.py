"""
cd /home/mamba/Scrivania


macchina1: ssh -i "chiavi_per_tesi.pem" ubuntu@ec2-16-171-171-11.eu-north-1.compute.amazonaws.com
IP: 16.171.171.11
rabbit@ip-172-31-47-21



macchina2: ssh -i "chiavi_per_tesi.pem" ubuntu@ec2-13-51-162-114.eu-north-1.compute.amazonaws.com
IP: 13.51.162.114


macchina3: ssh -i "chiavi_per_tesi.pem" ubuntu@ec2-13-53-39-10.eu-north-1.compute.amazonaws.com
IP: 13.53.39.10


macchina4: ssh -i "chiavi_per_tesi.pem" ubuntu@ec2-13-51-194-42.eu-north-1.compute.amazonaws.com
IP: 13.51.194.42


proxy: ssh -i "chiavi_per_tesi.pem" ubuntu@ec2-13-48-44-122.eu-north-1.compute.amazonaws.com
IP: 13.48.44.122


app.py<<<

from celery import Celery

import time

app = Celery(backend="redis://BlackMamba:Kobe@13.48.44.122:6379/0", broker="amqp://BlackMamba:Kobe@13.48.44.122:5672//")

@app.task
def preprocessing_task(sleeping_time):
    print("OK")
    time.sleep(sleeping_time)
    return "ok"

if __name__ == '__main__':
    app.start()



from celery import Celery

app = Celery(backend="redis://localhost:6379/0", broker="amqp://guest@localhost:5672//")



if __name__ == '__main__':
    app.start()


"""