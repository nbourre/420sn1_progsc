# Cours express sur la programmation <!-- omit in toc -->

# Table des matières <!-- omit in toc -->

- [Introduction](#introduction)
- [Les plans de leçons](#les-plans-de-leçons)
  - [Plan de leçon 1 : Introduction à la programmation et fonctions de base](#plan-de-leçon-1--introduction-à-la-programmation-et-fonctions-de-base)
  - [Plan de leçon 2 : Contrôle de flux et boucles](#plan-de-leçon-2--contrôle-de-flux-et-boucles)
  - [Plan de leçon 3 : Fonctions avancées et visualisation avec Matplotlib](#plan-de-leçon-3--fonctions-avancées-et-visualisation-avec-matplotlib)
- [Leçon 1 : Introduction à la programmation et fonctions de base](#leçon-1--introduction-à-la-programmation-et-fonctions-de-base)
  - [Objectifs](#objectifs)
  - [Contenu](#contenu)
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
  - [Objectifs](#objectifs-1)
  - [Contenu](#contenu-1)
  - [Révision des concepts abordés dans la première séance](#révision-des-concepts-abordés-dans-la-première-séance)
  - [Structures de contrôle de flux](#structures-de-contrôle-de-flux)
    - [Opérateurs de comparaison](#opérateurs-de-comparaison)
      - [Table de vérité](#table-de-vérité)
    - [Autres exemples](#autres-exemples)
  - [La valeur **`None`**](#la-valeur-none)
    - [Exemple d'utilisation de `None`](#exemple-dutilisation-de-none)
  - [Boucles](#boucles)
    - [Boucle `while`](#boucle-while)
    - [Boucle `for`](#boucle-for)

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

## Objectifs

-   Comprendre les concepts fondamentaux de la programmation.
-   Apprendre à utiliser l'outil de développement Thonny.
-   Créer des programmes simples pour effectuer des calculs.
-   Comprendre et créer des fonctions en Python.

## Contenu

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

---

**Exercice 1 : Conversion de température**
Écrivez une fonction appelée `convertir_c_en_f` qui prend une température en degrés Celsius en tant que paramètre et renvoie la température équivalente en degrés Fahrenheit. La formule de conversion est : $Fahrenheit = (Celsius × 9/5) + 32$.

**Exercice 2 : Calcul de la surface d'un rectangle**
Écrivez une fonction appelée `calculer_surface_rectangle` qui prend la longueur et la largeur d'un rectangle en tant que paramètres et renvoie sa surface.

-   Écrivez une fonction appelée `calculer_surface_carre` qui prend la longueur d'un côté d'un carré en tant que paramètre et renvoie sa surface. Cependant, utilisez la fonction `calculer_surface_rectangle` pour effectuer le calcul.


> **Devoir : Fonctions en lien avec votre domaine d'enseignement** <br />
> Quelle serait un cours sans devoir! Voici votre devoir :<br />
> 1. Écrivez quelques fonctions en lien avec votre domaine d'enseignement. Vous pouvez utiliser les exemples ci-dessus pour vous inspirer.<br />
> 2. Dans le prochain cours, nous allons voir les boucles. Pensez à des situations où vous aimeriez voir des calculs variant selon des paramètres. Par exemple, en physique, on peut calculer la vitesse finale d'un objet en chute libre en fonction de la hauteur de départ. Vous pouvez aussi trouver des situations où vous aimeriez voir des graphiques. Par exemple, en chimie, on peut tracer un graphique de la concentration d'une solution en fonction du temps.<br />
> 
> Vous pouvez me contacter via Teams pour regarder votre code et répondre à vos questions.

* * *

# Leçon 2 : Contrôle de flux et boucles

**Durée : 1 heure**

## Objectifs

-   Réviser les concepts abordés dans la première séance.
-   Apprendre à utiliser les structures de contrôle de flux.
-   Apprendre à utiliser la valeur `None`
-   Apprendre à utiliser les boucles.
-   Apprendre à utiliser Thonny pour déboguer les erreurs.
-   Créer des programmes avec des structures de contrôle et des boucles.

## Contenu

1.  **Bref retour sur les concepts abordés dans la première séance**
    -   Variables et types de données (entiers, flottants, chaînes de caractères).
    -   Opérations mathématiques en Python.
    -   Définition de fonctions en Python.
2.  **Structures de contrôle de flux**
3.  **La valeur `None`**
4.  **Boucles**
5.  **Exercices pratiques**
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

En français, on utilise les mots `si`, `sinon` et `sinon si` pour faire des choix. En programmation, on utilise les mots `if`, `else` et `elif` (*contraction de else if*).

Voici la structure générale de contrôle de flux :

```py
if condition:
    # Instructions
elif condition:
    # Instructions
else:
    # Instructions
```

Remarquez qu'après la condition, il y a un `:`. C'est la même chose pour les boucles. C'est une syntaxe spécifique à Python. On remarque aussi que les instructions sont indentées. C'est aussi une syntaxe spécifique à Python.

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
elif age < 65:
    print("Tarif adulte")
else:
    print("Tarif aîné")
```

Dans un `if`, il y a une condition. La condition est une expression booléenne. Une expression booléenne est une expression qui retourne `True` ou `False`. Si la condition est `True`, les instructions dans le `if` sont exécutées. Si la condition est `False`, les instructions dans le `if` sont ignorées.

Voici un exemple :

```py
# Variables
age = 18

if (age >= 18):
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

#### Table de vérité 
Voici un petit rappel de la table de vérité pour les opérateurs logiques `and` et `or` :

| `a`  | `b`  | `a and b` | `a or b` |
| :--: | :--: | :-------: | :------: |
| `T`  | `T`  |    `T`    |   `T`    |
| `T`  | `F`  |    `F`    |   `T`    |
| `F`  | `T`  |    `F`    |   `T`    |
| `F`  | `F`  |    `F`    |   `F`    |

En résumé pour le `ET`, il faut que les deux conditions soient vrai pour que l'expression soit vrai. Pour le `OU`, il faut qu'au moins une des conditions soit vrai pour que l'expression soit vrai.


### Autres exemples

Voici une liste d'exemples où l'on pourrait devoir utiliser des structures de contrôle de flux avec conditions multiples :
- **Science générale :** Trouver la bonne formule à appliquer selon les données d'entrée.
- **Géométrie :** Déterminer s'il y a collision entre deux rectangles.
- **Administration :** Déterminer si un étudiant est admissible à un programme.
- TODO: Ajouter des exemples avec les autres disciplines (Doit avoir des conditions multiples).


## La valeur **`None`**

En Python, il y a une valeur spéciale qui est `None`. Cette valeur est utilisée pour indiquer qu'une variable n'a pas de valeur. On peut l'utiliser pour initialiser une variable. On peut aussi l'utiliser pour indiquer qu'une fonction ne retourne pas de valeur.

Elle peut être utilisé pour initialiser une variable que l'on va utiliser plus tard. Par exemple, on peut utiliser `None` pour initialiser une variable qui va contenir le résultat d'un calcul.

### Exemple d'utilisation de `None`
Les opérateurs de comparaison en combinaison de `None` sont très utiles pour faire des choix. Par exemple dans le cas où l'on doit utiliser la bonne formule dépendant des données d'entrée.

Voici un exemple dans lequel on a différente fonction $PV=nRT$ dépendant des données d'entrée :

```py
# Variables
R = 0.0821  # Constante des gaz parfaits (L.atm/mol.K)

# Essayez de remplacer une valeur par None pour
# voir le résultat
n = 2.5     # Moles de gaz
T = 300     # Température en Kelvin
V = 10      # Volume en litres
P = None    # Pression en atm

msg = ''

# Structure de contrôle de flux
if n == None:
    # Cas où n est l'inconnue
    n = (P * V) / (R * T)
    msg = "Moles de gaz (n) :" + str(n)
elif T == None:
    # Cas où T est l'inconnue
    T = (P * V) / (R * n)
    msg = "Température (T) :" + str(T) + " K"
elif V == None:
    # Cas où V est l'inconnue
    V = (n * R * T) / P
    msg = "Volume (V) :" + str(V) + " L"
elif P == None:
    # Cas où P est l'inconnue
    P = (n * R * T) / V
    msg = "Pression (P) :" + str(P) + " atm"
else:
    # Cas où il y a une erreur
    msg = "Revérifiez vos données d'entrée. Il y a une erreur, car toutes les variables sont définies."

# Affichage du résultat
print ("Voici le résultat :")
print (msg)

```

// TODO: Ajouter des exemples avec des fonctions qui ont des paramètres optionnels.

---

## Boucles

Une boucle en programmation est une structure qui permet d'exécuter un bloc de code de manière répétée, généralement tant qu'une condition spécifiée est vraie. Cela permet d'automatiser la répétition d'une série d'instructions sans avoir à les écrire plusieurs fois.

Imaginez que vous ayez une tâche à accomplir plusieurs fois, comme compter de 1 à 10 ou afficher un message plusieurs fois. Plutôt que de copier et coller le même code encore et encore, vous pouvez utiliser une boucle pour effectuer cette tâche de manière efficace.

Il existe deux types principaux de boucles en programmation :

1. **La boucle `while` :** Cette boucle exécute un bloc de code tant qu'une condition spécifiée est vraie. Elle vérifie la condition avant d'entrer dans la boucle à chaque itération.

Voici un exemple simple en Python pour illustrer une boucle `while` :

```python
i = 1

while i <= 5:       # Tant que i est plus petit ou égal à 5
    print("Itération", i)
    i += 1          # On incrémente i de 1
```

> ***Nouveauté :*** L'opérateur `+=` permet d'incrémenter une variable. C'est l'équivalent de `somme = somme + note`.


2. **La boucle `for` :** Cette boucle itère sur une séquence (comme une liste, une plage de nombres, etc.) et exécute un bloc de code pour chaque élément de la séquence.

Voici un exemple simple en Python pour illustrer une boucle `for` :

```python
for i in range(1, 6):   # Pour i allant de 1 à 5
    print("Itération", i)
```

Dans cet exemple, la boucle `for` itère sur la séquence de nombres de 1 à 5. À chaque itération, le code à l'intérieur de la boucle est exécuté, affichant le message "Itération" suivi du numéro de l'itération.

> ***Nouveauté :*** `range(a, b)` est une fonction qui retourne une séquence de nombres de `a` à `b` où `b` est exclusif. On peut la traduire la plage de nombre entre `a` et `b` exclusif.
> 
> On peut aussi utiliser `range(6)` pour avoir une séquence de nombres de 0 à 5.

Les boucles sont un outil puissant pour automatiser des tâches répétitives et sont largement utilisées dans la programmation pour traiter des données, générer des motifs, et bien plus encore. Cependant, il est important de faire attention à la condition de sortie de la boucle pour éviter les boucles infinies (qui ne s'arrêtent jamais).

En effet, voici une boucle `while` qui ne s'arrête jamais :

```python
while True:
    print("Boucle infinie")
```
Pour l'arrêter, il faut appuyer sur le bouton `Stop` dans Thonny.

---

### Boucle `while`
La boucle `while` est utilisée pour exécuter un bloc de code tant qu'une condition spécifiée est vraie. Elle vérifie la condition avant d'entrer dans la boucle à chaque itération.

Elle se traduit en français par "tant que".

Souvent on l'utilise pour exécuter un bloc de code un nombre de fois indéterminé. On peut aussi l'utiliser pour exécuter un bloc de code tant qu'une condition est vraie.

Voici quelques exemples de code utilisant une boucle `while` :

```python
# Fonction qui affiche la somme des nombres de a à b
def calculer_somme_entre_borne(a, b):
    i = a
    somme = 0

    while i <= b:
        somme += i
        i += 1

    return somme

lim_inf = 1
lim_sup = 20

print ("Afficher la somme des nombres de", lim_inf, "à", lim_sup)
print ("Somme =", calculer_somme_entre_borne(lim_inf, lim_sup))

```

```python
# Fonction qui affiche les vitesses finales en fonction de la vitesse initiale,
# de l'accélération et du temps

def calculer_vf(v0, a, tf):
    vt = v0
    increment = 1
    t = 0

    while t <= tf:
        vt = v0 + a * t
        print("t =", t, "s, v =", vt, "m/s")
        t += increment

print ("Calcul de la vitesse finale en fonction de la vitesse initiale, de l'accélération et du temps")
v0 = float(input("Entrez la vitesse initiale (m/s) : "))
a = float(input("Entrez l'accélération (m/s^2) : "))
t = float(input("Entrez la durée en seconde : "))

calculer_vf(v0, a, t)
```

> ***Nouveauté :*** La fonction `input()` permet de demander une entrée à l'utilisateur. Elle retourne une chaîne de caractères. On doit donc convertir la chaîne de caractères en nombre pour pouvoir faire des calculs avec.
> 

> ***Nouveauté :*** La fonction `float()` permet de convertir une chaîne de caractères en nombre à virgule flottante. Il existe aussi la fonction `int()` pour convertir une chaîne de caractères en nombre entier.

Voici un exemple de boucle qui ne s'arrête que si la seconde entrée est plus grande que la première :

```python
# Demander deux nombres à l'utilisateur
# et afficher le plus grand des deux

print ("Afficher le plus grand des deux nombres")

a = float(input("Entrez un nombre : "))
b = float(input("Entrez un autre nombre : "))

while a >= b:
    print("Le premier nombre doit être plus petit que le deuxième.")
    a = float(input("Entrez un nombre : "))
    b = float(input("Entrez un autre nombre : "))

```

Voici un autre exemple qui calcule la moyenne de notes entrées par l'utilisateur :

```python
# Calculer la moyenne de notes entrées par l'utilisateur
print ("Calculer la moyenne de notes entrées par l'utilisateur")

note = 0
somme = 0
nb_notes = 0

while note != -1:
    note = float(input("Entrez une note (-1 pour terminer) : "))
    if note != -1:
        somme += note
        nb_notes += 1

moyenne = somme / nb_notes

print("La moyenne est", moyenne)
```

---

### Boucle `for`

TODO : Continuer pour la boucle `for`