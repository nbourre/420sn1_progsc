def calculer_somme_entre_borne(limite_inf, limite_sup):
    
    # Validation pour éviter des erreurs
    if not (isinstance(limite_inf, int) and isinstance(limite_sup, int)):
        return "Les deux limites doivent être de valeur entière."
    if limite_inf > limite_sup:
        return "La limite inférieure doit être plus petite que la limite supérieure."
    
    i = limite_inf
    somme = 0

    while i <= limite_sup:
        somme += i # Équivaut à somme = somme + i
        i += 1

    return somme

lim_inf = 1
lim_sup = 5

print ("Afficher la somme des nombres de", lim_inf, "à", lim_sup)
print ("Somme =", calculer_somme_entre_borne(lim_inf, lim_sup))