import json 

def get_meta(path):
    '''
    get_meta gets the relevant clinical metadata from the txt file
    
    :param path: path to json file with image metadada
    :return: list of meta data types (approx_age, anatom_site_general, benign_malignant, diagnosis, 
             diagnosis_confirm_type, melanocytic, sex)
    '''
    with open(path) as f:
        j = json.load(f)['meta']['clinical']
        return list(j.values())
