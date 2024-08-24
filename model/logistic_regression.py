from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, classification_report
import  joblib

def train_model(X_train, y_train):
    """
    entraine un model de regression logistique
    param: X_train, y_train
    param X_train: Caracteristique d'entrainement.
    param y_tain: cible d'entrainement
    return Pipeline contenant le preprocesseur et le model entrainer
    """
    numeric_feactures = ['age', 'température']
    categorical_feactures = ['sexe', 'symptômes']

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder()

    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_transformer, numeric_feactures), 
        ('cat', categorical_transformer, categorical_feactures)
        ])

    model = Pipeline(steps=[('preprocessoror', preprocessor),
                            ('classifier', LogisticRegression())
                            ])
    
    model.fit(X_train, y_train)
    return model
# end def

def evaluate_model(model, X_test, y_test):
    """
    Evalue le model sur l'ensemble de test. 
    :param moddel: Pipeline contenant le model entrainé.
    :param X_test: caracterisque de test. 
    :param y_test: ciible de test.  
    return None
    """
    y_pred = model.predict(X_test)
    print("Accurency:", accuracy_score(y_test, y_pred))
    print("Classification report:\n", classification_report(y_test, y_pred))
# end def
    
def save_model(model, filepath):
    """
    Sauvegarder le model entraîné.  
    :param model: Pipeline contenant le model entrîné
    :param filepath: chemain vers le fichier sauvegarder
    """
    joblib.dump(model, filepath)
# end def
    
def load_model(filepath):
    """
    charge le model sauvegardé

    :param filepath: Chemain vers le fichier de sauvegarde
    :return: Pipeline contenant le model chargé
    """
    return joblib.load(filepath)
# end def