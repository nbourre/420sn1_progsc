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
  - [Introduction aux fonctions - 45 minutes](#introduction-aux-fonctions---45-minutes)
    - [Définition de fonctions](#définition-de-fonctions)
    - [Extra : Règles de nomenclatures](#extra--règles-de-nomenclatures)
- [Leçon 2 : Contrôle de flux et boucles](#leçon-2--contrôle-de-flux-et-boucles)
  - [Objectifs :](#objectifs--1)
  - [Contenu :](#contenu--1)
  - [Révision des concepts abordés dans la première séance](#révision-des-concepts-abordés-dans-la-première-séance)
  - [Structures de contrôle de flux](#structures-de-contrôle-de-flux)
    - [Opérateurs de comparaison](#opérateurs-de-comparaison)
  - [Boucles](#boucles)

# Introduction

Cet article se veut comme un cours rapide sur les bases de la programmation pour pouvoir créer des outils. Il est destiné à des personnes qui ont déjà une base en science et qui veut utiliser la programmation pour faire des analyses de données, des calculs, des graphiques, etc. Il est aussi destiné à des personnes qui ont déjà une base en programmation mais qui veulent apprendre à utiliser Python. On prend aussi pour acquis que le lecteur connaît l'utilité de la programmation.

Ce cours est basé sur le langage Python. Il existe plusieurs langages de programmation, mais Python est un langage très populaire et très utilisé dans le monde de la science. Il est aussi très facile à apprendre et à utiliser. Il est donc un bon choix pour commencer à apprendre la programmation.

On séparera ce cours en trois leçons d'une heure. La première leçon se consacrera sur la programmation de base, la deuxième sur le contrôle de flux et boucles et la troisième sur les fonctions, les modules et l'affichage de graphiques.

# Les plans de leçons

## Plan de leçon 1 : Introduction à la programmation et fonctions de base

Durée : 1 heure

-   Introduction à la programmation et à Thonny.
-   Concepts fondamentaux de la programmation : variables, types de données, opérations mathématiques.
-   Écriture de programmes simples pour effectuer des calculs.
-   Introduction aux fonctions : définition, paramètres, valeurs de retour.
-   Exercices pratiques pour créer et appeler des fonctions simples.

## Plan de leçon 2 : Contrôle de flux et boucles

Durée : 1 heure

-   Révision des concepts abordés dans la première séance.
-   Structures de contrôle de flux : if, else, elif.
-   Utilisation de boucles : while et for.
-   Exercices pratiques pour créer des programmes avec des structures de contrôle et des boucles.
-   Introduction à l'utilisation de Thonny pour déboguer les erreurs.

## Plan de leçon 3 : Fonctions avancées et visualisation avec Matplotlib

Durée : 1 heure

-   Révision des concepts abordés dans les séances précédentes.
-   Fonctions avec des valeurs de retour et utilisation avancée de fonctions.
-   Introduction à la bibliothèque Matplotlib pour la visualisation de données.
-   Création de graphiques simples avec Matplotlib.
-   Exercices pratiques pour créer des programmes plus complexes avec des fonctions et générer des graphiques.

Chaque séance d'une heure se concentre sur des concepts spécifiques et propose des exercices pratiques pour renforcer les compétences acquises. Les plans seront adaptés en fonction du niveau de familiarité des enseignants avec la programmation.

* * *

# Leçon 1 : Introduction à la programmation et fonctions de base

**Durée : 1 heure**

## Objectifs :

-   Comprendre les concepts fondamentaux de la programmation.
-   Apprendre à utiliser l'outil de développement Thonny.
-   Créer des programmes simples pour effectuer des calculs.
-   Comprendre et créer des fonctions en Python.

## Contenu :

1.  **Introduction à la programmation et à Thonny**
    -   Présentation de l'interface Thonny.
    -   Présentation des concepts de base de la programmation.

2.  **Concepts fondamentaux de la programmation**
    -   Variables et types de données (entiers, flottants, chaînes de caractères).
    -   Opérations mathématiques en Python.

3.  **Écriture de programmes simples**
    -   Utilisation de l'éditeur Thonny pour écrire et exécuter du code.
    -   Création de programmes simples pour effectuer des calculs.

4.  **Introduction aux fonctions**
    -   Comprendre le concept de fonction.
    -   Définition de fonctions en Python.
    -   Paramètres et valeurs de retour des fonctions.

5.  **Exercices pratiques**
    -   Création de fonctions simples pour effectuer des calculs spécifiques.
    -   Appel de fonctions avec différents arguments.
    -   Utilisation de fonctions pour résoudre des problèmes simples.

## Introduction à la programmation et à Thonny - 5 minutes

-   La programmation est un moyen de donner des instructions à un ordinateur pour résoudre des problèmes.
-   Thonny est un environnement de développement Python qui facilite l'écriture, l'exécution et le débogage de code.

Voici une capture d'écran de Thonny avec un peu de code. Prenez quelques instants pour regarder l'interface et les différents éléments.

![Thonny avec un peu de code](img/99_thonny_pv_nrt.png?raw=true "Thonny avec un peu de code")

Vous reconnaissez probablement la formule ci-dessus soit la loi sur les gaz parfaits. Plus tard, nous allons utiliser cette formule pour faire des calculs simples.

### Installation de Thonny - 8 minutes

Pour l'installation de Thonny, on doit tout d'abord le télécharger sur le site officiel : <https://thonny.org/>

![Alt text](img/01a_download.gif)

Il n'est pas nécessaire d'être administrateur pour installer Thonny. Vous pouvez donc l'installer sur votre ordinateur personnel.

> **Note :** L'installateur est en anglais, mais l'interface de Thonny est disponible en français. Lors de la première exécution, l'outil vous demandera de choisir la langue de l'interface.

Vidéo montrant l'installation de Thonny

[![Installation de Thonny](https://img.youtube.com/vi/jYAvJqxHs5E/hqdefault.jpg)](https://www.youtube.com/watch?v=jYAvJqxHs5E)

Premier démarrage de Thonny

![Alt text](img/99_thonny_premier_dem.png)

### Tour d'horizon de Thonny - 10 minutes

Thonny est un environnement de travail qui est très simple à utiliser. Il est donc parfait pour les débutants. Dans cette section, nous allons faire un tour d'horizon de Thonny.

Lorsque vous ouvrez Thonny, vous devriez voir une fenêtre qui ressemble à ceci :

![Thonny avec un peu de code](img/99_thonny_pv_nrt.png?raw=true "Thonny avec un peu de code")

Comme la majorité des applications Windows, on retrouve une barre de menu en haut de la fenêtre. Cette barre de menu contient les menus suivants :

-   `Fichier` : Contient les options pour créer, ouvrir, enregistrer et imprimer un fichier.
-   `Éditer` : Contient les options pour copier, couper, coller et annuler.
-   `Affichage` : Contient les options pour afficher ou masquer les différents panneaux de Thonny.
-   `Exécuter` : Contient les options pour exécuter le code.
-   `Outils` : Contient les options pour configurer Thonny.
-   `Aide` : Contient les options pour obtenir de l'aide sur Thonny.

En dessous de la barre de menu, on retrouve une barre d'outils. Cette barre d'outils contient les boutons suivants :

-   `Nouveau` : Permet de créer un nouveau fichier.
-   `Ouvrir` : Permet d'ouvrir un fichier existant.
-   `Enregistrer` : Permet d'enregistrer le fichier courant.
-   **`Exécuter`** : Permet d'exécuter le code.
-   `Déboguer` : Permet de déboguer le code.
    -   Quelques boutons en lien avec le débogage sont grisés. Nous verrons en cours de session comment les utiliser.
-   `Arrêter` : Permet d'arrêter l'exécution du code.

En dessous de la barre d'outils, on retrouve la fenêtre principale de Thonny. Lors de la première exécution, cette fenêtre est divisée en deux parties :

-   La partie du haut est l'éditeur de code. C'est dans cette partie que vous allez écrire votre code.
-   La partie du bas est la console. C'est dans cette partie que vous allez voir le résultat de l'exécution de votre code.

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

* * *

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

-   **Commentaires :**
    -   Le symbole `#` est utilisé pour faire des commentaires. Tout ce qui suit le symbole `#` sur une ligne est ignoré par l'interpréteur Python. Ils sont utilisés pour expliquer le code et rendre le code plus lisible. 
-   **Variables :**
    -   Dans les premières lignes, on remarque des lettres (`n`, `R`, `T` et `V`) suivis du symbole `=`. Ces lignes sont des déclarations de variables.
    -   Une variable est un espace mémoire qui contient une valeur. Dans le cas présent les valeurs sont de type numérique. Ces valeurs peuventt être de différents types. Nous verrons les types de données plus loin.
    -   Pour pouvoir faire des calculs, on doit utiliser des variables. Les variables sont utilisées pour stocker des valeurs qui seront utilisées dans des calculs.
-   **L'assignation :**
    -   Le symbole `=` est utilisé pour assigner une valeur à une variable. On appelle cela l'assignation.
    -   L'assignation est une opération qui consiste à stocker une valeur dans une variable.
    -   L'assignation se fait de la façon suivante : `variable = valeur`
    -   L'assignation se fait de la droite vers la gauche. La valeur est assignée à la variable.
-   **Expressions :**
    -   La lignes `P = (n * R * T) / V` est une expression arithmétique dont la valeur est assignée à la variable `P`. Une expression est une combinaison de valeurs, de variables et d'opérateurs. Lorsque l'interpréteur Python évalue une expression, il produit une valeur.
    -   En programmation, la priorité des opérations est la même qu'en mathématiques. Les opérations entre parenthèses sont effectuées en premier, les exposants, et ainsi de suite.
-   **Affichage :**
    -   La fonction `print()` est utilisée pour afficher du texte et des valeurs à l'écran.
    -   Elle peut prendre plusieurs paramètres séparés par des virgules. Elle affichera les paramètres séparés par un espace.
        -   `print("Bonjour", "tout", "le", "monde")` affichera `Bonjour tout le monde`.
        -   Dans l'exemple précédent, la ligne `print("Température (T) :", T, "K")` affichera `Température (T) : 300 K`.

### Les opérateurs mathématiques

Voici un tableau des opérateurs mathématiques de base en Python :

| Opérateur | Description                                          | Exemple  |
| :-------: | :--------------------------------------------------- | :------- |
|    `+`    | Addition                                             | `2 + 3`  |
|    `-`    | Soustraction                                         | `2 - 3`  |
|    `*`    | Multiplication                                       | `2 * 3`  |
|    `/`    | Division                                             | `2 / 3`  |
|    `**`   | Exposant                                             | `2 ** 3` |
|    `//`   | Division entière (Donne le quotient de la division.) | `2 // 3` |
|    `%`    | Modulo (Donne le reste de la division.)              | `2 % 3`  |

* * *

## Écriture de programmes simples - 10 minutes

Modifiez le code précédent pour trouver une solution propre à votre domaine d'enseignement.

Quelques idées :

-   **Physique :** Vitesse d'un objet en chute libre.
-   **Chimie :** Concentration d'une solution.
-   **Mathématiques :** Calcul de la moyenne de notes.
-   **Biologie :** Calcul de l'indice de masse corporelle.

* * *

## Introduction aux fonctions - 45 minutes

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

* * *

### Définition de fonctions

Python offre plusieurs fonctions de base, mais souvent on doit créer nos propres fonctions pour effectuer des tâches spécifiques. Voici un exemple de fonction calculant le sinus d'un angle en degrés :

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

Pour créer une fonction, on doit utiliser une syntaxe spécifique.

La syntaxe générale pour créer une fonction est la suivante :

```py
def nom_de_la_fonction([paramètres [, ...]]):
    # Instructions
    return valeur_de_retour
```

-   Le mot-clé `def` est utilisé pour définir une fonction.
-   Le nom de la fonction doit être unique. Il est recommandé d'utiliser un nom qui décrit la fonction.
-   Les paramètres sont des valeurs qui sont passées à la fonction. **Les paramètres sont optionnels**. Si la fonction ne prend pas de paramètres, on doit quand même mettre les parenthèses.
    -   Les paramètres sont séparés par des virgules.
    -   Les paramètres sont des variables locales à la fonction. Elles ne sont pas accessibles à l'extérieur de la fonction.
-   `return` est utilisé pour retourner une valeur à l'appelant. Si la fonction ne retourne pas de valeur, `return` est optionnel.
    -   `return` termine l'exécution de la fonction.
    -   `return` peut retourner une valeur ou une expression.
    -   `return` peut retourner plusieurs valeurs séparées par des virgules.
    -   `return` peut être utilisé pour retourner une valeur avant la fin de la fonction.

> **Note :** Dans la littérature technique, les caractères `[]` indiquent que le contenu est optionnel. Dans la syntaxe ci-dessus, les paramètres sont optionnels. On peut donc écrire `def nom_de_la_fonction():` si la fonction ne prend pas de paramètres.

Aspects importants à retenir :

-   Une fonction ne fait rien tant qu'elle n'est pas appelée.
-   Les lignes de code qui définissent une fonction doivent être indentées.
    -   L'indentation est le fait de décaler le texte vers la droite.
    -   L'indentation est généralement de 4 espaces.
    -   L'indentation est utilisée pour définir les blocs de code.
    -   L'indentation est utilisée pour rendre le code plus lisible.
    -   L'indentation est obligatoire en Python.

Voici quelques exemples de fonctions :

```py
import datetime
import math

# Fonction affichant un message
def afficher_erreur():
    print("Il y a une erreur, veuillez recommencer!")
    # Le return optionnel ici, car 
    # on ne fait qu'afficher un message

# Fonction retournant l'heure du système
def get_heure():
    # Il faudra importer le module datetime
    # pour utiliser cette fonction
    return datetime.datetime.now().time()

# Aire d'un cercle
def calculer_aire_cercle(rayon):
  return 3.14159 * rayon ** 2

# Fonction retournant la moyenne de trois nombres
def calculer_moyenne(a, b, c):
  somme = (a + b + c)
  return somme / 3

# Fonction retournant la vitesse finale en fonction
# de la vitesse initiale, de l'accélération et du temps
def calculer_vitesse_finale(v0, a, t):
  vt = a * t
  return v0 + vt

# Fonction retournant l'énergie potentielle
def calculer_energie_potentielle(m, dY):
  return m * 9.8 * dY

# Fonction retournant l'énergie cinétique
def calculer_energie_cinetique(m, v):
  return (m * v ** 2) / 2

# Fonction retournant l'énergie mécanique
def calculer_energie_mecanique(m, v, dY):
  # On peut utiliser des fonctions dans d'autres fonctions
  ek = energie_cinetique(m, v)
  ep = energie_potentielle(m, dY)
  return ek + ep

# Fonction retournant la pression
def calculer_pression(n, R, T, V):
  return (n * R * T) / V

# Fonction retournant la masse finale d'un échantillon en fonction
# de sa masse initiale, du temps et de la demi-vie
def calculer_decroissance_exponentielle(m0, t, demi_vie):
    return m0 * math.exp(-t / demi_vie)

# Exemple d'utilisation
afficher_erreur()
print( get_heure())
print (calculer_moyenne (65, 23, 12))
print (calculer_aire_cercle(5))
print (calculer_vitesse_finale(10, 5, 2))
print (calculer_energie_potentielle(10, 5))
print (calculer_energie_cinetique(10, 5))
print (calculer_energie_mecanique(10, 5, 2))
print (calculer_pression(2.5, 0.0821, 300, 10))
print (calculer_decroissance_exponentielle(100, 10, 5))
```

On remarque que la syntaxe est toujours similaire et respecte les règles énoncées plus haut.

### Extra : Règles de nomenclatures

En plus des règles de syntaxes, les langages de programmations ont tous des règles de nomenclatures. Ces règles sont des conventions qui permettent de rendre le code plus lisible. Vous remarquez que les fonctions débutent tous par un verbe. Voici quelques règles de nomenclatures pour Python:

-   Les noms de fonctions ou variables doivent être en minuscules.
-   Les noms de fonctions ou variables doivent être séparés par des underscores (trait souligné).
-   Si c'est une action, le nom de la fonction doit débuter par un verbe.

Pour la majorité des langages de programmation, les règles de nomenclatures sont les suivantes :

-   Les noms ne doivent contenir que des lettres, des chiffres et des underscores (\_).
-   Les noms ne doivent pas débuter par un chiffre.
-   Les noms doivent être en un seul mot, i.e. aucun espace.

Voici un tableau d'exemples valides et non valides :

| Nom Valide         | Nom non valide                                             |
| :----------------- | :--------------------------------------------------------- |
| `balance_actuelle` | `balance-actuelle` (Le tirait n'est pas valide)            |
| `niveauPH`         | `niveau pH` (Les espaces ne sont pas permis)               |
| `vitesse0`         | `0vitesse` (Ne peut pas débuter avec un chiffre)           |
| `_42`              | `42` (Ne peut pas débuter avec un chiffre)                 |
| `total_somme`      | `total_$omme` (Les caractères spéciaux ne sont pas permis) |
| `densite`          | `densité` (Les accents sont proscrits)                     |

* * *

**Exercice 1 : Conversion de température**
Écrivez une fonction appelée `convertir_c_en_f` qui prend une température en degrés Celsius en tant que paramètre et renvoie la température équivalente en degrés Fahrenheit. La formule de conversion est : $Fahrenheit = (Celsius × 9/5) + 32$.

**Exercice 2 : Calcul de la surface d'un rectangle**
Écrivez une fonction appelée `calculer_surface_rectangle` qui prend la longueur et la largeur d'un rectangle en tant que paramètres et renvoie sa surface.

-   Écrivez une fonction appelée `calculer_surface_carre` qui prend la longueur d'un côté d'un carré en tant que paramètre et renvoie sa surface. Cependant, utilisez la fonction `calculer_surface_rectangle` pour effectuer le calcul.

**Exercice 3 : Fonctions en lien avec votre domaine d'enseignement**
Écrivez quelques fonctions en lien avec votre domaine d'enseignement. Vous pouvez utiliser les exemples ci-dessus pour vous inspirer.

* * *

# Leçon 2 : Contrôle de flux et boucles

**Durée : 1 heure**

## Objectifs :

-   Réviser les concepts abordés dans la première séance.
-   Apprendre à utiliser les structures de contrôle de flux.
-   Apprendre à utiliser les boucles.
-   Apprendre à utiliser Thonny pour déboguer les erreurs.
-   Créer des programmes avec des structures de contrôle et des boucles.

## Contenu :

1.  **Bref retour sur les concepts abordés dans la première séance**
    -   Variables et types de données (entiers, flottants, chaînes de caractères).
    -   Opérations mathématiques en Python.
    -   Définition de fonctions en Python.
2.  **Structures de contrôle de flux**
3.  **Boucles**
4.  **Exercices pratiques**
    -   Création de programmes avec des structures de contrôle et des boucles.
    -   Utilisation de Thonny pour déboguer les erreurs.

## Révision des concepts abordés dans la première séance

Voici quelques questions pour réviser les concepts abordés dans la première séance :

1.  Qu'est-ce qu'une variable?
2.  Qu'est-ce que l'assignation?
3.  Qu'est-ce qu'une expression?
4.  Qu'est-ce qu'une fonction?
5.  Qu'est-ce que l'indentation?
6.  Quelles sont les règles générales de nomenclatures en Python?

## Structures de contrôle de flux

Les structures de contrôle de flux permettent de contrôler l'exécution du code. Elles permettent de faire des choix selon des conditions. Elles permettent aussi de répéter des instructions.

En français, on utilise les mots `si`, `sinon` et `sinon si` pour faire des choix. En programmation, on utilise les mots `if`, `else` et `elif`.

Voici la structure générale de contrôle de flux :

```py
if condition:
    # Instructions
elif condition:
    # Instructions
else:
    # Instructions
```

**Seul le `if` est obligatoire**. On peut avoir plusieurs `elif` et un seul `else`. On peut aussi avoir seulement un `if` et un `else`.

Voici un exemple que vous pouvez tester:

```py
# Variables
age = 18

# Structure de contrôle de flux
if age < 5:
    print("Gratuit")
elif age < 12:
    print("Tarif enfant")
elif age < 65
    print("Tarif adulte")
else:
    print("Tarif aîné")
```

Dans un `if`, il y a une condition. La condition est une expression booléenne. Une expression booléenne est une expression qui retourne `True` ou `False`. Si la condition est `True`, les instructions dans le `if` sont exécutées. Si la condition est `False`, les instructions dans le `if` sont ignorées.

Voici un exemple :

```py
# Variables
age = 18

est_adulte = age >= 18

if (est_adulte):
    print("Vous êtes un adulte")
else:
    print("Vous êtes un mineur")
```

On peut mettre des structures conditionnelles à l'intérieur des fonctions.

Voici un exemple :

```py
# Fonction indiquant si le pH est acide, neutre ou basique
def type_pH(pH):
    if pH < 7:
        print("Acide")
    elif pH > 7:
        print("Basique")
    else:
        print("Neutre")

# Appel de la fonction
type_pH(7.5)
```

> **Note :** On remarque toujours l'indentation dans les structures de contrôle de flux. Cela facilite la lecture en bloc. On rappel que l'indentation est obligatoire en Python.

### Opérateurs de comparaison

Les expressions conditionnelles utilisent des opérateurs de comparaison. Voici un tableau des opérateurs de comparaison de base :

| Opérateur | Description          | Exemple   |
| :-------: | :------------------- | :-------- |
|    `==`   | Égalité              | `a == b`  |
|    `!=`   | Différence           | `a != b`  |
|    `>`    | Plus grand que       | `a > b`   |
|    `<`    | Plus petit que       | `a < b`   |
|    `>=`   | Plus grand ou égal à | `a >= b`  |
|    `<=`   | Plus petit ou égal à | `a <= b`  |
|   `not`   | Négation             | `not a`   |
|   `and`   | ET logique           | `a and b` |
|    `or`   | OU logique           | `a or b`  |

Dans tous les cas, l'expression retourne `True` ou `False`. `a` ou `b` peuvent être des variables ou des expressions.

Voici un exemple :

```py
# Variables
age = 18
ami = True

# Structure de contrôle de flux
if age >= 18 and ami:
    print("On va au Trou du Diable!")
else:
    print("On reste à la maison")
```

// TODO: Ajouter des exemples avec des fonctions qui ont des paramètres optionnels.

## Boucles

* * *
