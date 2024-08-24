# Covid-19 Prediction

## Description

Ce projet est une application qui utilise des données de covid-19 pour prédire si une personne a ou non la covid-19.

## Objectif

L'objectif de ce projet est de créer un modèle de régression logistique qui peut prédire si une personne a ou non la covid-19.

## Prérequis

- Python 3.8
- pip
- pip install -r requirements.txt

## Utilisation

### 1. Trainer le modèle

```shell
    python main.py
```

### 2. Prédire si une personne a la covid-19

```shell
python predict.py
```

### 3. Structurer les données

```csv
    age,sexe,température,symptômes,a_covid
```

### 4. Structure du Projet

```arduino
covid_predict
    ├── data
    │   ├── __init__.py
    │   └── generate_data.py
    ├── model
    │   ├── __init__.py
    │   └── logistic_regression.py
    ├── utils
    │   ├── __init__.py
    │   └── presualization.py
    ├── covid_data.csv
    ├── main.py
    ├── predict.py
    ├── requirements.txt
    └── README.md

```

### 5. Auteur

[Vincent-Kaleba](https://github.com/vincentkaleba)
