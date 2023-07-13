from celery import Celery
from email.mime.text import MIMEText

from controllers.create_config_dict import create_config_dict
from controllers.run_marco import run_experiment

import smtplib

celery = Celery(backend="redis://localhost:6379/0", broker="amqp://guest@localhost:5672//")


@celery.task
def preprocessing_task(dataset, receiver):
    #config = create_config_dict(dataset)  # creo dizionario di configurazione da cui creare un namespace
    #preprocessed_dataset = run_experiment(config)
    # grazie al dizionario costruirò un namespace che darò al run per ottenere il dataset preprocessato
    #request_no = config['experiment']['splitting']['save_folder'].split('splitted_data/')[1]
    sender_address = "dmncelery@gmail.com"
    password = "maeudeefdzsqsmyx"

    object = "Celery preprocessing_task completed"
    body = "Gentile utente, il task celery da lei avviato è stato completato"

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
    try:
        print("ok")
    except smtplib.SMTPException as e:
        print("Errore durante l'invio dell'email:", e)


"""
print("OK")
    time.sleep(sleeping_time)
    return "ok"
"""
