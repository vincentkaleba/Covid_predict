from data.generate_data import load_data
from model.logistic_regression import train_model, evaluate_model, save_model
from utils.visualization import plot_class_distribution
from sklearn.model_selection import train_test_split

def main():
    """
    Purpose: 
    """
    data = load_data('covid_data.csv')

    X = data.drop('a_covid', axis=1)
    y = data['a_covid']

    plot_class_distribution(y) #Visualiser la distribution des classes

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) #distributions des données

    model = train_model(X_train, y_train) #entraînement du model

    evaluate_model(model, X_test, y_test) #evaluation du model

    save_model(model, 'model.pkl')
# end def
    
if __name__=='__main__':
    main()