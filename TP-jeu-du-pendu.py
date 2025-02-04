# TP : Jeu du pendu
# -----------------------------------
# Objectif : Écrire un programme en Python qui permet de jouer au jeu du pendu. Le programme doit choisir un mot au hasard dans une liste prédéfinie, puis demander au joueur de deviner les lettres de ce mot. Le joueur a un nombre limité d’essais pour trouver le mot. Si le joueur dépasse ce nombre sans avoir trouvé le mot, il perd.

# 1 - Importer le module random
# 2 - Créer une liste de mots
# 3 - Choisir un mot au hasard
# 4 - Décomposer le mot en lettres
# 5 - Demander au joueur de deviner une lettre
import random

listeDeMots = ['pomme', 'voiture', 'chien', 'chat', 'maison', 'ordinateur', 'table', 'chaise', 'fenetre', 'porte']

mot = random.choice(listeDeMots)
tailleMot = len(mot)
motCache = ['_'] * tailleMot 

score = 0
nombreEssais = 0

print(' '.join(motCache))

while score < tailleMot and nombreEssais < 10:  
    inputLettre = input('Entrez une lettre : ').lower()

    if inputLettre in mot:
        occurences = 0  
        for i in range(tailleMot):
            if mot[i] == inputLettre and motCache[i] == '_':  # Vérifie si la lettre est déjà révélée
                motCache[i] = inputLettre
                occurences += 1  
        
        score += occurences  
        print(f'La lettre "{inputLettre}" est dans le mot !\n')
    else:
        print(f'La lettre "{inputLettre}" n\'est pas dans le mot.\n')
    
    nombreEssais += 1
    nombreEssaisRestant = 10 - nombreEssais
    print(f"Mot actuel : {' '.join(motCache)}")
    print(f"Essais restants : {nombreEssaisRestant}\n")

if score == tailleMot:
    print(f'Félicitations ! Tu as trouvé le mot : {mot}')
else:
    print(f'Perdu ! Le mot était : {mot}')
