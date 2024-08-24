import pandas as pd
from model.logistic_regression import load_model

def get_user_input():
    """
    Obtient les données de la nouvelle personne
    :return dataFrame: contenant les données saisis par l'utilisateur
    """
    age  = int(input("Entrer l'âge: "))
    sexe = input("Entrer le sexe (H/F): ").upper()
    température = float(input("Entrer la température en °F: "))
    symptômes = input("Entrer les symptômes (toux, fièvren, essouflement, mal_de_tête, fatigue) : ").lower()

    data = pd.DataFrame({
        'age': [age],
        'sexe': [sexe],
        'température': [température],
        'symptômes': [symptômes]
    })
    return data
# end def

def predict_new_data(model_path):
    """
    Fait des predictions sur de nouvelles données saisis par  l'utilisateur.  
    :param model_path: Chemain vers le model sauvegarder
    :return None
    """
    new_data = get_user_input() #obtenir les nouvelles données

    model = load_model(model_path) #charger le model sauvegarder

    predictions = model.predict(new_data)

    for i, pred in enumerate(predictions):
        print(f"Prédiction : {'A COVID-19' if pred == 1 else 'Pas de COVID-19'}")
# end def
        
if __name__=="__main__":
    predict_new_data('model.pkl')