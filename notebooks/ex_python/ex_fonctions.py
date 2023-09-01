import datetime

# Fonction affichant un message
def afficher_erreur():
    print("Il y a une erreur, veuillez recommencer!")


# Fonction retournant l'heure du système
def heure():
    # Il faudra importer le module datetime
    # pour utiliser cette fonction
    return datetime.datetime.now().time()

# Fonction retournant la somme de deux nombres
def somme(a, b):
    return a + b

# Fonction retournant la moyenne de trois nombres
def moyenne(a, b, c):
    return (a + b + c) / 3

# Fonction retournant le plus grand de deux nombres
def plus_grand(a, b):
    if a > b:
        return a
    else:
        return b

# Exemple d'utilisation
print( heure())
print (somme (5, 4))
print (moyenne (65, 23, 12))
print (plus_grand (203, 12))