# Leçon 4 : Manipulation de données <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Objectifs](#objectifs)
- [Lire des fichiers locaux](#lire-des-fichiers-locaux)
- [Lire un fichier texte](#lire-un-fichier-texte)
  - [Exercices](#exercices)
- [Lire un fichier CSV avec `pandas`](#lire-un-fichier-csv-avec-pandas)
  - [Utiliser `pandas` pour lire un fichier CSV](#utiliser-pandas-pour-lire-un-fichier-csv)
  - [Fonctions courantes pour manipuler des données avec `pandas`](#fonctions-courantes-pour-manipuler-des-données-avec-pandas)
- [Leçon bonus : ChatGPT](#leçon-bonus--chatgpt)
- [Références](#références)


# Objectifs
- Apprendre à lire des fichiers locaux en utilisant Python.
- Afficher des données de manière à faciliter leur copie vers Excel.
- Enregistrer des données dans des fichiers au format CSV et Excel.
- Afficher des graphiques pour visualiser des données.

# Lire des fichiers locaux
Savoir lire dans un fichier est une compétence fondamentale en programmation. Cela permet de lire des données et de les manipuler dans un programme.

Voici quelques raisons pour lesquelles il est important de savoir lire des fichiers :

- **Accès aux Données** : Essentiel pour exploiter les données nécessaires aux analyses.
- **Automatisation** : Permet le traitement automatisé de grandes quantités de données.
- **Interdisciplinarité** : Facilite la collaboration et l'utilisation de données entre différents domaines.
- **Reproductibilité** : Contribue à la reproductibilité des recherches en permettant la vérification des résultats.
- **Adaptabilité** : Rend capable de gérer divers types de données et formats de fichiers.
- **Exploitation des Ressources** : Ouvre l'accès à une vaste quantité de ressources éducatives et scientifiques.
- **Économie de Ressources** : Économise le temps et les efforts, permettant de se concentrer sur l'analyse et l'innovation.

# Lire un fichier texte
Pour lire un fichier texte, on utilise la fonction `open()` avec le mode `r` pour lire. On peut ensuite utiliser la méthode `read()` pour lire le contenu du fichier.

Voici un exemple permettant de lire de contenu d'un fichier texte :

```python
# Déclarer le chemin vers le fichier
nom_fichier = "fichier.txt"

# Initialiser le contenu
contenu = ""

# Ouvrir le fichier en mode lecture
with open(nom_fichier, "r") as fichier:
    contenu = fichier.read()

# Afficher le contenu
print(contenu)
```

---

Remarquez dans l'exemple précédent que l'on utilise le mot-clé `with`. Cela permet de s'assurer que le fichier est fermé après avoir été utilisé. C'est une bonne pratique en programmation de fermer les fichiers après les avoir utilisés.

> **Note** : Le chemin vers le fichier peut être absolu ou relatif. Un chemin absolu est le chemin complet vers le fichier. Un chemin relatif est le chemin par rapport à l'emplacement du script Python.
> 
> Il est possible d'utilise ce format de chemin pour Windows : `c:/dossier/fichier.txt`. Il est plus facile que le format standard `c:\\dossier\\fichier.txt`.

---

Nous avons utilisé la méthode `read()` pour lire le contenu du fichier. Il existe d'autres méthodes pour lire le contenu d'un fichier. Par exemple, on peut utiliser la méthode `readline()` pour lire une ligne à la fois.

Voici un exemple :

```python
# Déclarer le nom du fichier
nom_fichier = "fichier.txt"

# Ouvrir le fichier en mode lecture
with open(nom_fichier, "r") as fichier:
    # Lire la première ligne
    ligne = fichier.readline()
    print(ligne)

    # Lire la deuxième ligne
    ligne = fichier.readline()

```

L'utilisation de `readline()` est utile pour lire un fichier ligne par ligne. Cela peut être utile pour traiter des fichiers volumineux.

## Exercices
1. Allez à cette adresse : https://www.kaggle.com/datasets/reihanenamdari/breast-cancer/data
2. Téléchargez le fichier : "Breast_Cancer.csv"
   - Plus bas dans la page où l'on voit le tableau
     ![alt text](assets/04_breast_cancer_dl.png)
3. Enregistrez le fichier dans le même dossier que votre script Python.
4. Modifiez le script de l'exemple précédent pour lire le contenu du fichier `Breast_Cancer.csv`.
5. Exécutez le script et observez l'information qui défile.

---

# Lire un fichier CSV avec `pandas`
Dans l'exercice précédent, vous avez téléchargé un fichier en format CSV. Un fichier CSV (*Comma-Separated Values*) est un fichier texte qui contient des données séparées par des séparateurs qui sont généralement des virgule, des points-virgules ou des tabulations. C'est un format de fichier couramment utilisé pour stocker des données tabulaires.

On utilise souvent ce format pour stocker des données provenant de bases de données ou pour échanger des données entre différentes applications.

Le format ressemble un peu à un tableau Excel. Chaque ligne du fichier correspond à une ligne du tableau et chaque valeur est séparée par un séparateur.

D'ailleurs, Excel peut ouvrir des fichiers CSV.

Voici un exemple de contenu CSV :

```csv
Nom,Prénom,Âge
Tremblay,Marie,25
Lavoie,Éric,32
Gagnon,Stéphanie,28
```

Dans plusieurs cas, la première ligne du fichier CSV contient les noms des colonnes. Cela permet de savoir ce que chaque colonne représente.

Pour lire un fichier CSV, on peut utiliser la librairie `pandas`. C'est une librairie très populaire pour manipuler des données en Python.

## Utiliser `pandas` pour lire un fichier CSV
Voici un exemple pour lire un fichier CSV avec `pandas` :

```python
# Importer la librairie pandas et lui donner l'alias pd
import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("Breast_Cancer.csv")

# Afficher les 5 premières lignes
print(df.head())
```

Voici la sortie de l'exemple :

```
>>> %Run -c $EDITOR_CONTENT
   Age   Race Marital Status  ... Reginol Node Positive Survival Months Status
0   68  White        Married  ...                     1              60  Alive
1   50  White        Married  ...                     5              62  Alive
2   58  White       Divorced  ...                     7              75  Alive
3   58  White        Married  ...                     1              84  Alive
4   47  White        Married  ...                     1              50  Alive

[5 rows x 16 columns]
>>> 
```

On voit que `pandas` a lu le fichier et affiché les 5 premières lignes de ce fichier. C'est très utile pour voir rapidement le contenu du fichier.

> **Note** : Dans l'importation de `pandas`, on lui a donné l'alias `pd`. C'est une convention très courante en Python. Cela permet de raccourcir le nom de la librairie pour l'utiliser plus facilement.

---

On remarque que l'on travaille avec la variable `df`. C'est une variable de type `DataFrame` de `pandas`.

Le `DataFrame` pandas est une structure qui contient des données bidimensionnelles et leurs étiquettes correspondantes. Les `DataFrames` sont largement utilisés dans la science des données, l'apprentissage automatique, le calcul scientifique et de nombreux autres domaines intensifs en données. Les `DataFrames` sont similaires aux tables SQL ou aux feuilles de calcul avec lesquelles vous travaillez dans Excel ou Calc.



## Fonctions courantes pour manipuler des données avec `pandas`
`pandas` offre plusieurs fonctions pour manipuler des données. Voici quelques exemples :

| Fonction | Description |
| --- | --- |
| `df.head()` | Affiche les 5 premières lignes du tableau. |
| `df.tail()` | Affiche les 5 dernières lignes du tableau. |
| `df.info()` | Affiche des informations sur le tableau. |
| `df.describe()` | Affiche des statistiques sur le tableau. |
| `df.shape` | Retourne le nombre de lignes et de colonnes du tableau. |
| `df.columns` | Retourne les noms des colonnes du tableau. |
| `df['Nom de la colonne']` | Retourne une colonne du tableau. |

---
Voici ce que retourne `df.info()` :

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4024 entries, 0 to 4023
Data columns (total 16 columns):
 #   Column                  Non-Null Count  Dtype 
---  ------                  --------------  ----- 
 0   Age                     4024 non-null   int64 
 1   Race                    4024 non-null   object
 2   Marital Status          4024 non-null   object
 3   T Stage                 4024 non-null   object
 4   N Stage                 4024 non-null   object
 5   6th Stage               4024 non-null   object
 6   differentiate           4024 non-null   object
 7   Grade                   4024 non-null   object
 8   A Stage                 4024 non-null   object
 9   Tumor Size              4024 non-null   int64 
 10  Estrogen Status         4024 non-null   object
 11  Progesterone Status     4024 non-null   object
 12  Regional Node Examined  4024 non-null   int64 
 13  Reginol Node Positive   4024 non-null   int64 
 14  Survival Months         4024 non-null   int64 
 15  Status                  4024 non-null   object
dtypes: int64(5), object(11)
memory usage: 503.1+ KB
None
```

TODO : Ajouter un exemple de lecture de fichier CSV avec `pandas`.
TODO : Ajouter les fonctions de base pour manipuler des données avec `pandas`.

# Leçon bonus : ChatGPT
- Utiliser ChatGPT pour nous aider à faire du code

---

# Références
- [Introducing the pandas DataFrame](https://realpython.com/pandas-dataframe/)