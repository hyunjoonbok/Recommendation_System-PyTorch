from models.ItemKNN import ItemKNN
from models.SLIM import SLIM
from models.BPRMF import BPRMF
from models.MultVAE import MultVAE

def build_model(model_name, model_conf, num_users, num_items, device):
    if model_name =='BPRMF':
        model = BPRMF(model_conf, num_users, num_items, device)
    elif model_name == 'MultVAE':
        model = MultVAE(model_conf, num_users, num_items, device)
    elif model_name == 'SLIM':
        model = SLIM(model_conf, num_users, num_items, device)
    elif model_name == 'ItemKNN':
        model = ItemKNN(model_conf, num_users, num_items, device)
    else:
        raise NotImplementedError('Choose a Model.')

    return model