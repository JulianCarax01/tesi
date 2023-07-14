"""
Module description:

"""

__version__ = '0.3.1'
__author__ = 'Vito Walter Anelli, Claudio Pomo'
__email__ = 'vitowalter.anelli@poliba.it, claudio.pomo@poliba.it'

import importlib
from os import path
import numpy as np

from elliot.namespace.namespace_model_builder import NameSpaceBuilder

_rstate = np.random.RandomState(42)
here = path.abspath(path.dirname(__file__) + '/../')
def run_experiment(config_dict):

    builder = NameSpaceBuilder(config_dict, here, here) #modifica rispetto alla versione tradizionale di elliot
    base = builder.base

    dataloader_class = getattr(importlib.import_module("elliot.dataset"),
                               "DataSetLoader")
    # la funzione import_module importa il modulo di cui specifichiamo il path, nello specifico di tale modulo vogliamo l'attributo
    # DataSetLoader
    dataloader = dataloader_class(base.base_namespace)
    data_test_list = dataloader.generate_dataobjects() #i nostri risultati

    return data_test_list
