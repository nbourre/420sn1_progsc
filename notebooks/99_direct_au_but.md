# Cours express sur la programmation <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Les plans de leçons](#les-plans-de-leçons)
  - [Plan de leçon 1 : Introduction à la programmation et fonctions de base](#plan-de-leçon-1--introduction-à-la-programmation-et-fonctions-de-base)
  - [Plan de leçon 2 : Contrôle de flux et boucles](#plan-de-leçon-2--contrôle-de-flux-et-boucles)
  - [Plan de leçon 3 : Fonctions avancées et visualisation avec Matplotlib](#plan-de-leçon-3--fonctions-avancées-et-visualisation-avec-matplotlib)
- [Plan de leçon 1 : Introduction à la programmation et fonctions de base](#plan-de-leçon-1--introduction-à-la-programmation-et-fonctions-de-base-1)
  - [Objectifs :](#objectifs-)
  - [Contenu :](#contenu-)
  - [Introduction à la programmation et à Thonny](#introduction-à-la-programmation-et-à-thonny)
    - [Installation de Thonny](#installation-de-thonny)
- [Exercices :](#exercices-)


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

# Plan de leçon 1 : Introduction à la programmation et fonctions de base
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

## Introduction à la programmation et à Thonny
- La programmation est un moyen de donner des instructions à un ordinateur pour résoudre des problèmes.
- Thonny est un environnement de développement Python qui facilite l'écriture, l'exécution et le débogage de code.

Voici une capture d'écran de Thonny avec un peu de code. Prenez quelques instants pour regarder l'interface et les différents éléments.

![Thonny avec un peu de code](img/99_thonny_pv_nrt.png?raw=true "Thonny avec un peu de code")

Vous reconnaissez probablement la formule ci-dessus soit la loi sur les gaz parfaits. Plus tard, nous allons utiliser cette formule pour faire des calculs simples.

### Installation de Thonny
Pour l'installation de Thonny, on doit tout d'abord le télécharger sur le site officiel : https://thonny.org/

Il n'est pas nécessaire d'être administrateur pour installer Thonny. Vous pouvez donc l'installer sur votre ordinateur personnel.

> **Note :** L'installateur est en anglais, mais l'interface de Thonny est disponible en français. Lors de la première exécution, l'outil vous demandera de choisir la langue de l'interface.

{% include youtube.html id="jYAvJqxHs5" %}

<video src="https://www.youtube.com/watch?v=jYAvJqxHs5E"></video>

![Installer Thonny](https://www.youtube.com/watch?v=jYAvJqxHs5E)

<video src="img/99_thonny_installation.mp4" controls title="Title"></video>

![Alt text](img/99_thonny_premier_dem.png)


Voici le code copiable pour faire le calcul de la pression d'un gaz parfait :

```python
# Données d'entrée
n = 2.5     # Moles de gaz
R = 0.0821  # Constante des gaz parfaits (L.atm/mol.K)
T = 300     # Température en Kelvin
V = 10      # Volume en litres

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



# Exercices :

**Exercice 1 : Calcul de la moyenne**
Écrivez une fonction appelée `calculer_moyenne` qui prend trois nombres en tant que paramètres et renvoie la moyenne de ces nombres.

**Exercice 2 : Conversion de température**
Écrivez une fonction appelée `celsius_en_fahrenheit` qui prend une température en degrés Celsius en tant que paramètre et renvoie la température équivalente en degrés Fahrenheit. La formule de conversion est : Fahrenheit = (Celsius × 9/5) + 32.

**Exercice 3 : Calcul de la surface d'un rectangle**
Écrivez une fonction appelée `calculer_surface_rectangle` qui prend la longueur et la largeur d'un rectangle en tant que paramètres et renvoie sa surface.


