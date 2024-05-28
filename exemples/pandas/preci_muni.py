import pandas as pd
import matplotlib.pyplot as plt


# Chemin vers le fichier CSV contenant les données des normales climatiques mensuelles de Québec
chemin_fichier = 'D:/OneDrive - Cégep de Shawinigan/_cours/_contenus/SN1 - Programmation en sciences/github/420sn1_progsc/data/csv/normales-mens-1991-2020.csv'

# Charger les données à partir du fichier CSV en utilisant Pandas
donnees_climatiques = pd.read_csv(chemin_fichier)

# Demander à l'utilisateur d'entrer le nom de la ville
nom_ville = input("Entrez le nom de la ville pour laquelle vous souhaitez filtrer les données : ")

# Filtrer les données pour les villes qui contiennent le nom spécifié par l'utilisateur
donnees_ville = donnees_climatiques[donnees_climatiques['NOM_STATION'].str.contains(nom_ville, case=False)]


# Vérifier si des données ont été trouvées pour la ville spécifiée
if donnees_ville.empty:
    print("Aucune donnée n'est disponible pour la station de {}.".format(nom_ville))
else:
    # Extraire les colonnes de mois, neige normale, pluie normale, température maximale normale et température minimale normale
    mois = donnees_ville["MOIS"]
    neige_normale = donnees_ville["NEIGE_NORMALE"]
    pluie_normale = donnees_ville["PLUIE_NORMALE"]
    tmax_normale = donnees_ville["TMAX_NORMALE"]
    tmin_normale = donnees_ville["TMIN_NORMALE"]


    # Créer un graphique
    fig, ax1 = plt.subplots()

    # Tracer les données de neige normale et pluie normale sur l'axe Y1
    ax1.plot(mois, neige_normale, label='Neige normale', color='blue')
    ax1.plot(mois, pluie_normale, label='Pluie normale', color='orange')
    ax1.set_xlabel('Mois')
    ax1.set_ylabel('Neige et pluie normales')
    ax1.tick_params(axis='y')

    # Créer un deuxième axe Y pour les températures
    ax2 = ax1.twinx()
    ax2.plot(mois, tmax_normale, label='Température maximale normale', color='green', linestyle='--')
    ax2.plot(mois, tmin_normale, label='Température minimale normale', color='red', linestyle='--')
    ax2.set_ylabel('Températures normales')
    ax2.tick_params(axis='y')


    # Placer la légende dans le coin supérieur gauche
    fig.tight_layout()
    plt.legend(loc='best')

    # Afficher le graphique
    plt.title('Moyenne mensuelle des conditions climatiques normales pour {}'.format(nom_ville))
    plt.show()


