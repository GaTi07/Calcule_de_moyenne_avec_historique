# Créé par PEREIRA, le 05/10/2023 en Python 3.7
import random

# Générer une liste de 500 nombres décimaux aléatoires entre 0 et 1
nombres_decimaux = [round(random.uniform(0, 1), 2) for _ in range(500)]

# Convertir la liste en une chaîne de caractères avec des virgules
liste_en_chaine = ",".join(map(str, nombres_decimaux))

# Afficher la chaîne
print(liste_en_chaine)

