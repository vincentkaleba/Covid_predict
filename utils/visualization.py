import matplotlib.pyplot as plt

def plot_class_distribution(y):
    """
    Visualise la distribution de classes.   
    :param y: Cible(lasses)
    :return: None
    """
    plt.figure(figsize=(8, 6))
    y.value_counts().plot(kind='bar')
    plt.title('Nombre d\'exemples')
    plt.show()
# end def