from celery import Celery
from email.mime.text import MIMEText

from controllers.create_config_dict import create_config_dict
from controllers.run_marco import run_experiment

import smtplib
import pandas as pd

dataset = pd.read_csv("dataset-3.tsv", sep="\t")

app = Celery(backend="redis://13.48.44.122:6379/0", broker="amqp://BlackMamba:Kobe@13.48.44.122:5672//")


def send_email(receiver, string):
    try:
        sender_address = "dmncelery@gmail.com"
        password = "maeudeefdzsqsmyx"

        object = "Celery preprocessing_task completed"
        body = "Gentile utente, il task celery da lei avviato è stato completato: " + string

        email = smtplib.SMTP("smtp.gmail.com", 587)
        email.ehlo()
        email.starttls()
        email.login(sender_address, password)

        message = MIMEText(body, 'plain', 'utf-8')
        message['Subject'] = object
        message['From'] = sender_address
        message['To'] = receiver
        email.sendmail(sender_address, receiver, message.as_string())
        email.quit()
    except smtplib.SMTPException as e:
        print("Errore durante l'invio dell'email:", e)


@app.task
def preprocessing_task(receiver):
    config = create_config_dict(dataset)  # creo dizionario di configurazione da cui creare un namespace
    preprocessed_dataset = run_experiment(config)
    request_no = config['experiment']['splitting']['save_folder'].split('splitted_data/')[1]
    sender_address = "dmncelery@gmail.com"
    password = "maeudeefdzsqsmyx"

    object = "Celery preprocessing_task completed"
    body = "Gentile utente, il task celery da lei avviato è stato completato: " + request_no

    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email.login(sender_address, password)

    message = MIMEText(body, 'plain', 'utf-8')
    message['Subject'] = object
    message['From'] = sender_address
    message['To'] = receiver
    email.sendmail(sender_address, receiver, message.as_string())
    email.quit()


if __name__ == '__main__':
    app.start()