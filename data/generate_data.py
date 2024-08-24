import pandas as pd

def load_data(filepath):
    """
    Cette function charge les donnée depuis un fichier csv  
    param: filepath - chemain vers le fichier csv (covid_data.csv) 
    return dataFrame contenantles données
    """
    data = pd.read_csv(filepath)
    return data
# end def