"""
Module description:

"""

__version__ = '0.3.1'
__author__ = 'Vito Walter Anelli, Claudio Pomo'
__email__ = 'vitowalter.anelli@poliba.it, claudio.pomo@poliba.it'

import importlib
from os import path
#import numpy as np
from elliot.namespace.namespace_model_builder import NameSpaceBuilder

#_rstate = np.random.RandomState(42)
here = path.abspath(path.dirname(__file__) + '/../')
"""
print(u'''
__/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\___/\\\\\\\\\\\\______/\\\\\\\\\\\\_________________________________________        
 _\\/\\\\\\///////////___\\////\\\\\\_____\\////\\\\\\_________________________________________       
  _\\/\\\\\\_________________\\/\\\\\\________\\/\\\\\\______/\\\\\\_____________________/\\\\\\______      
   _\\/\\\\\\\\\\\\\\\\\\\\\\_________\\/\\\\\\________\\/\\\\\\_____\\///_______/\\\\\\\\\\______/\\\\\\\\\\\\\\\\\\\\\\_     
    _\\/\\\\\\///////__________\\/\\\\\\________\\/\\\\\\______/\\\\\\____/\\\\\\///\\\\\\___\\////\\\\\\////__    
     _\\/\\\\\\_________________\\/\\\\\\________\\/\\\\\\_____\\/\\\\\\___/\\\\\\__\\//\\\\\\_____\\/\\\\\\______   
      _\\/\\\\\\_________________\\/\\\\\\________\\/\\\\\\_____\\/\\\\\\__\\//\\\\\\__/\\\\\\______\\/\\\\\\_/\\\\__  
       _\\/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\___/\\\\\\\\\\\\\\\\\\___/\\\\\\\\\\\\\\\\\\__\\/\\\\\\___\\///\\\\\\\\\\/_______\\//\\\\\\\\\\___ 
        _\\///////////////___\\/////////___\\/////////___\\///______\\/////__________\\/////____''')

print(f'Version Number: {__version__}')

"""
def run_experiment(config_dict):
    builder = NameSpaceBuilder(config_dict, here, here)  # modifica rispetto alla versione tradizionale di elliot
    base = builder.base

    dataloader_class = getattr(importlib.import_module("elliot.dataset"),
                               "DataSetLoader")
    # la funzione import_module importa il modulo di cui specifichiamo il path, nello specifico di tale modulo vogliamo l'attributo
    # DataSetLoader
    dataloader = dataloader_class(
        base.base_namespace)  # Passare il namespace di configurazione costruito a partire dal dizionario config
    data_test_list = dataloader.generate_dataobjects()  # i nostri risultati

    return data_test_list
