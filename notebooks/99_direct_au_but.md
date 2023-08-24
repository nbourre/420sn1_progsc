# Cours express sur la programmation <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Les plans de leçons](#les-plans-de-leçons)
  - [Plan de leçon 1 : Introduction à la programmation et fonctions de base](#plan-de-leçon-1--introduction-à-la-programmation-et-fonctions-de-base)
  - [Plan de leçon 2 : Contrôle de flux et boucles](#plan-de-leçon-2--contrôle-de-flux-et-boucles)
  - [Plan de leçon 3 : Fonctions avancées et visualisation avec Matplotlib](#plan-de-leçon-3--fonctions-avancées-et-visualisation-avec-matplotlib)
- [Leçon 1 : Introduction à la programmation et fonctions de base](#leçon-1--introduction-à-la-programmation-et-fonctions-de-base)
  - [Objectifs :](#objectifs-)
  - [Contenu :](#contenu-)
  - [Introduction à la programmation et à Thonny - 5 minutes](#introduction-à-la-programmation-et-à-thonny---5-minutes)
    - [Installation de Thonny - 8 minutes](#installation-de-thonny---8-minutes)
    - [Tour d'horizon de Thonny - 10 minutes](#tour-dhorizon-de-thonny---10-minutes)
    - [Tester Thonny](#tester-thonny)
  - [Concepts fondamentaux de la programmation](#concepts-fondamentaux-de-la-programmation)
    - [Les opérateurs mathématiques](#les-opérateurs-mathématiques)
  - [Écriture de programmes simples - 10 minutes](#écriture-de-programmes-simples---10-minutes)
  - [Introduction aux fonctions](#introduction-aux-fonctions)
    - [Définition de fonctions](#définition-de-fonctions)
- [À compléter :](#à-compléter-)


# Introduction

Cet article se veut comme un cours rapide sur les bases de la programmation pour pouvoir créer des outils. Il est destiné à des personnes qui ont déjà une base en science et qui veut utiliser la programmation pour faire des analyses de données, des calculs, des graphiques, etc. Il est aussi destiné à des personnes qui ont déjà une base en programmation mais qui veulent apprendre à utiliser Python. On prend aussi pour acquis que le lecteur connaît l'utilité de la programmation.

Ce cours est basé sur le langage Python. Il existe plusieurs langages de programmation, mais Python est un langage très populaire et très utilisé dans le monde de la science. Il est aussi très facile à apprendre et à utiliser. Il est donc un bon choix pour commencer à apprendre la programmation.

On séparera ce cours en trois leçons d'une heure. La première leçon se consacrera sur la programmation de base, la deuxième sur le contrôle de flux et boucles et la troisième sur les fonctions, les modules et l'affichage de graphiques.

# Les plans de leçons
## Plan de leçon 1 : Introduction à la programmation et fonctions de base
Durée : 1 heure

- Introduction à la programmation et à Thonny.
- Concepts fondamentaux de la programmation : variables, types de données, opérations mathématiques.
- Écriture de programmes simples pour effectuer des calculs.
- Introduction aux fonctions : définition, paramètres, valeurs de retour.
- Exercices pratiques pour créer et appeler des fonctions simples.

## Plan de leçon 2 : Contrôle de flux et boucles
Durée : 1 heure

- Révision des concepts abordés dans la première séance.
- Structures de contrôle de flux : if, else, elif.
- Utilisation de boucles : while et for.
- Exercices pratiques pour créer des programmes avec des structures de contrôle et des boucles.
- Introduction à l'utilisation de Thonny pour déboguer les erreurs.

## Plan de leçon 3 : Fonctions avancées et visualisation avec Matplotlib
Durée : 1 heure

- Révision des concepts abordés dans les séances précédentes.
- Fonctions avec des valeurs de retour et utilisation avancée de fonctions.
- Introduction à la bibliothèque Matplotlib pour la visualisation de données.
- Création de graphiques simples avec Matplotlib.
- Exercices pratiques pour créer des programmes plus complexes avec des fonctions et générer des graphiques.

Chaque séance d'une heure se concentre sur des concepts spécifiques et propose des exercices pratiques pour renforcer les compétences acquises. Les plans seront adaptés en fonction du niveau de familiarité des enseignants avec la programmation.

---

# Leçon 1 : Introduction à la programmation et fonctions de base
**Durée : 1 heure**

## Objectifs :

- Comprendre les concepts fondamentaux de la programmation.
- Apprendre à utiliser l'outil de développement Thonny.
- Créer des programmes simples pour effectuer des calculs.
- Comprendre et créer des fonctions en Python.

## Contenu :

1. **Introduction à la programmation et à Thonny**
   - Présentation de l'interface Thonny.
   - Présentation des concepts de base de la programmation.

2. **Concepts fondamentaux de la programmation**
   - Variables et types de données (entiers, flottants, chaînes de caractères).
   - Opérations mathématiques en Python.

3. **Écriture de programmes simples**
   - Utilisation de l'éditeur Thonny pour écrire et exécuter du code.
   - Création de programmes simples pour effectuer des calculs.

4. **Introduction aux fonctions**
   - Comprendre le concept de fonction.
   - Définition de fonctions en Python.
   - Paramètres et valeurs de retour des fonctions.

5. **Exercices pratiques**
   - Création de fonctions simples pour effectuer des calculs spécifiques.
   - Appel de fonctions avec différents arguments.
   - Utilisation de fonctions pour résoudre des problèmes simples.

## Introduction à la programmation et à Thonny - 5 minutes
- La programmation est un moyen de donner des instructions à un ordinateur pour résoudre des problèmes.
- Thonny est un environnement de développement Python qui facilite l'écriture, l'exécution et le débogage de code.

Voici une capture d'écran de Thonny avec un peu de code. Prenez quelques instants pour regarder l'interface et les différents éléments.

![Thonny avec un peu de code](img/99_thonny_pv_nrt.png?raw=true "Thonny avec un peu de code")

Vous reconnaissez probablement la formule ci-dessus soit la loi sur les gaz parfaits. Plus tard, nous allons utiliser cette formule pour faire des calculs simples.

### Installation de Thonny - 8 minutes
Pour l'installation de Thonny, on doit tout d'abord le télécharger sur le site officiel : https://thonny.org/

![Alt text](img/01a_download.gif)

Il n'est pas nécessaire d'être administrateur pour installer Thonny. Vous pouvez donc l'installer sur votre ordinateur personnel.

> **Note :** L'installateur est en anglais, mais l'interface de Thonny est disponible en français. Lors de la première exécution, l'outil vous demandera de choisir la langue de l'interface.

Vidéo montrant l'installation de Thonny

[![Installation de Thonny](https://img.youtube.com/vi/jYAvJqxHs5E/hqdefault.jpg)](https://www.youtube.com/watch?v=jYAvJqxHs5E)

<iframe width="560" height="315" src="https://www.youtube.com/embed/jYAvJqxHs5E?si=vQO_gPyny8_GWC9-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Premier démarrage de Thonny

![Alt text](img/99_thonny_premier_dem.png)

### Tour d'horizon de Thonny - 10 minutes
Thonny est un environnement de travail qui est très simple à utiliser. Il est donc parfait pour les débutants. Dans cette section, nous allons faire un tour d'horizon de Thonny.

Lorsque vous ouvrez Thonny, vous devriez voir une fenêtre qui ressemble à ceci :

![Thonny avec un peu de code](img/99_thonny_pv_nrt.png?raw=true "Thonny avec un peu de code")

Comme la majorité des applications Windows, on retrouve une barre de menu en haut de la fenêtre. Cette barre de menu contient les menus suivants :
- `Fichier` : Contient les options pour créer, ouvrir, enregistrer et imprimer un fichier.
- `Éditer` : Contient les options pour copier, couper, coller et annuler.
- `Affichage` : Contient les options pour afficher ou masquer les différents panneaux de Thonny.
- `Exécuter` : Contient les options pour exécuter le code.
- `Outils` : Contient les options pour configurer Thonny.
- `Aide` : Contient les options pour obtenir de l'aide sur Thonny.

En dessous de la barre de menu, on retrouve une barre d'outils. Cette barre d'outils contient les boutons suivants :
- `Nouveau` : Permet de créer un nouveau fichier.
- `Ouvrir` : Permet d'ouvrir un fichier existant.
- `Enregistrer` : Permet d'enregistrer le fichier courant.
- **`Exécuter`** : Permet d'exécuter le code.
- `Déboguer` : Permet de déboguer le code.
  - Quelques boutons en lien avec le débogage sont grisés. Nous verrons en cours de session comment les utiliser.
- `Arrêter` : Permet d'arrêter l'exécution du code.

En dessous de la barre d'outils, on retrouve la fenêtre principale de Thonny. Lors de la première exécution, cette fenêtre est divisée en deux parties :
- La partie du haut est l'éditeur de code. C'est dans cette partie que vous allez écrire votre code.
- La partie du bas est la console. C'est dans cette partie que vous allez voir le résultat de l'exécution de votre code.

### Tester Thonny
Pour tester Thonny, nous allons écrire un petit programme qui calcule la pression d'un gaz parfait. Voici le code à coller dans l'éditeur de code :

```python
# Variables
# Données d'entrée
n = 2.5     # Moles de gaz
R = 0.0821  # Constante des gaz parfaits (L.atm/mol.K)
T = 300     # Température en Kelvin
V = 10      # Volume en litres

# Formules
# Calcul de la pression en utilisant la formule PV = nRT
P = (n * R * T) / V

# Affichage du résultat
print("Données d'entrée:")
print("Moles de gaz (n) :", n)
print("Constante des gaz (R) :", R)
print("Température (T) :", T, "K")
print("Volume (V) :", V, "L")

print("\nCalcul de la pression (P) :")
print("Pression (P) =", P, " atm")
```

Appuyez sur le bouton `Exécuter` (ou `Play`) pour exécuter le code. Vous devriez voir le résultat dans la console.

L'analyse du code se fera dans la partie suivante.

---

## Concepts fondamentaux de la programmation
Dans cette section, nous allons voir les concepts fondamentaux de la programmation. Nous allons voir les variables, les types de données et les opérations mathématiques.

Voici le code que nous avons écrit dans la section précédente :

```py
# Variables
# Données d'entrée
n = 2.5     # Moles de gaz
R = 0.0821  # Constante des gaz parfaits (L.atm/mol.K)
T = 300     # Température en Kelvin
V = 10      # Volume en litres

# Formules
# Calcul de la pression en utilisant la formule PV = nRT
P = (n * R * T) / V

# Affichage du résultat
print("Données d'entrée:")
print("Moles de gaz (n) :", n)
print("Constante des gaz (R) :", R)
print("Température (T) :", T, "K")
print("Volume (V) :", V, "L")

print("\nCalcul de la pression (P) :")
print("Pression (P) =", P, " atm")
```

- **Commentaires :**
  - Le symbole `#` est utilisé pour faire des commentaires. Tout ce qui suit le symbole `#` sur une ligne est ignoré par l'interpréteur Python. Ils sont utilisés pour expliquer le code et rendre le code plus lisible. 
- **Variables :**
  - Dans les premières lignes, on remarque des lettres (`n`, `R`, `T` et `V`) suivis du symbole `=`. Ces lignes sont des déclarations de variables.
  - Une variable est un espace mémoire qui contient une valeur. Dans le cas présent les valeurs sont de type numérique. Ces valeurs peuventt être de différents types. Nous verrons les types de données plus loin.
  - Pour pouvoir faire des calculs, on doit utiliser des variables. Les variables sont utilisées pour stocker des valeurs qui seront utilisées dans des calculs.
- **L'assignation :**
  - Le symbole `=` est utilisé pour assigner une valeur à une variable. On appelle cela l'assignation.
  - L'assignation est une opération qui consiste à stocker une valeur dans une variable.
  - L'assignation se fait de la façon suivante : `variable = valeur`
  - L'assignation se fait de la droite vers la gauche. La valeur est assignée à la variable.
- **Expressions :**
  - La lignes `P = (n * R * T) / V` est une expression arithmétique dont la valeur est assignée à la variable `P`. Une expression est une combinaison de valeurs, de variables et d'opérateurs. Lorsque l'interpréteur Python évalue une expression, il produit une valeur.
  - En programmation, la priorité des opérations est la même qu'en mathématiques. Les opérations entre parenthèses sont effectuées en premier, les exposants, et ainsi de suite.
- **Affichage :**
  - La fonction `print()` est utilisée pour afficher du texte et des valeurs à l'écran.
  - Elle peut prendre plusieurs paramètres séparés par des virgules. Elle affichera les paramètres séparés par un espace.
    - `print("Bonjour", "tout", "le", "monde")` affichera `Bonjour tout le monde`.
    - Dans l'exemple précédent, la ligne `print("Température (T) :", T, "K")` affichera `Température (T) : 300 K`.


### Les opérateurs mathématiques
Voici un tableau des opérateurs mathématiques de base en Python :

| Opérateur | Description | Exemple |
| :---: | :--- | :--- |
| `+` | Addition | `2 + 3` |
| `-` | Soustraction | `2 - 3` |
| `*` | Multiplication | `2 * 3` |
| `/` | Division | `2 / 3` |
| `**` | Exposant | `2 ** 3` |
| `//` | Division entière (Donne le quotient de la division.) | `2 // 3` |
| `%` | Modulo (Donne le reste de la division.) | `2 % 3` |

---

## Écriture de programmes simples - 10 minutes
Modifiez le code précédent pour trouver une solution propre à votre domaine d'enseignement.

Quelques idées :
- **Physique :** Vitesse d'un objet en chute libre.
- **Chimie :** Concentration d'une solution.
- **Mathématiques :** Calcul de la moyenne de notes.
- **Biologie :** Calcul de l'indice de masse corporelle.

---

## Introduction aux fonctions
Dans cette section, nous allons voir les fonctions. Nous allons voir ce qu'est une fonction, comment la définir et comment l'appeler.

Une fonction est un bloc de code qui effectue une tâche spécifique. Une fonction peut prendre des paramètres en entrée et peut retourner une valeur en sortie. Une fonction peut être appelée à partir d'un autre code pour effectuer une tâche spécifique.

Par exemple sur les calculatrices scientifiques, on retrouve les fonctions trigonométriques. Ces fonctions prennent un angle en entrée et retournent la valeur du sinus, du cosinus ou de la tangente de cet angle.

Python fournit les fonctions de mathématiques de base dans le module `math`. Pour utiliser ces fonctions, on doit importer le module `math` dans notre code. Voici un exemple :

```py
# Importation du module math
import math

angle = 45
rad = math.radians(angle)
resultat = math.sin(rad)

print("Sinus de", angle, "degrés :", resultat)
```

> **Note :** Nous verrons en détail l'importation de modules dans une leçon future.

**Analyse du code**

```py
import math
```

Cette ligne importe le module `math` dans notre code. Cela nous permet d'utiliser les fonctions du module `math`.

```py
angle = 45
rad = math.radians(angle)  
```

Ces lignes définissent une variable `angle` et assignent la valeur `45` à cette variable. La ligne suivante définit une variable `rad` et assigne la valeur de la fonction `math.radians(angle)` à cette variable. La fonction `math.radians(angle)` prend un angle en degrés en entrée et retourne la valeur de cet angle en radians.

Les ordinateurs utilisent les radians pour faire des calculs trigonométriques. Il est donc nécessaire de convertir les angles en radians avant de faire des calculs trigonométriques.

```py
resultat = math.sin(rad)
```

Cette ligne définit une variable `resultat` et assigne la valeur de la fonction `math.sin(rad)` à cette variable. La fonction `math.sin(rad)` prend un angle en radians en entrée et retourne la valeur du sinus de cet angle.

```py
print("Sinus de", angle, "degrés :", resultat)
```

Cette ligne affiche le résultat du calcul. La fonction `print()` prend plusieurs paramètres en entrée et affiche ces paramètres à l'écran. Dans le cas présent, la fonction `print()` affiche le texte `Sinus de`, la valeur de la variable `angle`, le texte `degrés :` et la valeur de la variable `resultat`.

---

### Définition de fonctions
Python offre plusieurs fonctions de base, mais souvent on doit créer nos propres fonctions pour effectuer des tâches spécifiques. Pour créer une fonction, on doit utiliser une syntaxe spécifique. Voici un exemple de fonction calculant le sinus d'un angle en degrés :

```py
def sinus(angle):
    rad = math.radians(angle)
    resultat = math.sin(rad)
    return resultat

angleA = 45
resultatA = sinus(angleA)

angleB = 60
resultatB = sinus(angleB)


print("Sinus de", angleA, "degrés :", resultatA)
print("Sinus de", angleB, "degrés :", resultatB)
```


// TODO : Ajouter une explication de la syntaxe








// TODO : Ajouter des exercices
# À compléter :

**Exercice 1 : Calcul de la moyenne**
Écrivez une fonction appelée `calculer_moyenne` qui prend trois nombres en tant que paramètres et renvoie la moyenne de ces nombres.

**Exercice 2 : Conversion de température**
Écrivez une fonction appelée `celsius_en_fahrenheit` qui prend une température en degrés Celsius en tant que paramètre et renvoie la température équivalente en degrés Fahrenheit. La formule de conversion est : Fahrenheit = (Celsius × 9/5) + 32.

**Exercice 3 : Calcul de la surface d'un rectangle**
Écrivez une fonction appelée `calculer_surface_rectangle` qui prend la longueur et la largeur d'un rectangle en tant que paramètres et renvoie sa surface.


