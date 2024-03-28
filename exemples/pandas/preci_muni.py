import pandas as pd

# Chemin vers le fichier CSV contenant les données des normales climatiques mensuelles de Québec
chemin_fichier = 'D:/OneDrive - Cégep de Shawinigan/_cours/_contenus/SN1 - Programmation en sciences/github/420sn1_progsc/data/csv/normales-mens-1991-2020.csv'

# Charger les données à partir du fichier CSV en utilisant Pandas
donnees_climatiques = pd.read_csv(chemin_fichier)

# Afficher les premières lignes du DataFrame pour s'assurer que les données ont été chargées correctement
print(donnees_climatiques.info())

