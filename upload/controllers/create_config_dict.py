import os
import shutil
from datetime import datetime
import hashlib  # se proprio dopo vogliamo farla con hash il nome del dataset
from flask import Flask, request
import zipfile  # per gestire lo zip inviato nella strategia hierarchy
import json


# questa funzione viene utilizzata per creare un dizionario di configurazione a partire dall'oggetto richiesta proveniente dal client
# TO DO sistemare il bug con il fixed timestamp
# TO DO sistemare il bug nel temporal hold out


def create_config_dict(dataset):
    config = dict()
    config['experiment'] = dict()
    config['experiment']['data_config'] = dict()
    config['experiment']['data_config']['strategy'] = "dataset"
    timestamp = datetime.now()
    timestamp_string = timestamp.strftime("%d-%m-%Y-%H-%M-%S")
    cript = hashlib.md5((timestamp_string + 'request/').encode('utf-8'))
    _path = 'data/' + cript.hexdigest()
    os.makedirs(_path, exist_ok=False)
    dataset_path = _path + '/dataset.tsv'

    #    dataset.save(dataset_path)

    # with open(dataset_path, "w") as file:
    #    json.dump(dataset, file)

    dataset.to_csv(dataset_path, sep="\t", index=False)

    config['experiment']['data_config']['dataset_path'] = dataset_path

    config['experiment']['splitting'] = dict()
    config['experiment']['splitting']['test_splitting'] = dict()
    config['experiment']['prefiltering'] = []
    config['experiment']['splitting']['test_splitting']['strategy'] = "random_subsampling"
    config['experiment']['splitting']['test_splitting']['test_ratio'] = 0.2
    config['experiment']['splitting']['test_splitting']['folds'] = 1
    """
    config['experiment']['splitting']['validation_splitting'] = dict()
    config['experiment']['splitting']['validation_splitting']['strategy'] = None
    """
    config['experiment']['dataset'] = "dataset-3"
    save_folder = 'splitted_data/' + cript.hexdigest()
    config['experiment']['splitting']['save_on_disk'] = True
    config['experiment']['splitting']['save_folder'] = save_folder
    config['experiment']['random_seed'] = 42
    config['experiment']['binarize'] = False
    return config
