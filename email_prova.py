import smtplib
import pandas
from email.mime.text import MIMEText


from controllers.create_config_dict import create_config_dict
from controllers.run_marco import run_experiment

ds = pandas.read_csv("dataset-3.tsv", sep="\t")
dataset_list = ds.values.tolist()

receiver = "alexandros0117@gmail.com"

config = create_config_dict(dataset_list)  # creo dizionario di configurazione da cui creare un namespace
preprocessed_dataset = run_experiment(
    config)  # grazie al dizionario costruirò un namespace che darò al run per ottenere il dataset preprocessato
request_no = config['experiment']['splitting']['save_folder'].split('splitted_data/')[1]
sender_address = "dmncelery@gmail.com"
password = "maeudeefdzsqsmyx"

object = "Celery preprocessing_task completed"
body = "Gentile utente, il task celery da lei avviato è stato completato" + request_no

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
