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

lettres = list(mot)

tailleMot = len(mot)

for i in range(tailleMot):
    lettres[i] = '_'


score = 0
nombreEssais = 0

while score < tailleMot and nombreEssais < 10:  
    inputLettre = input('Entrez une lettre : ')
    if inputLettre in mot:
        score += 1
        nombreEssais += 1
        nombreEssaisRestant = 10 - nombreEssais
        print('La lettre est dans le mot, il vous reste ', nombreEssaisRestant, ' essais \n')
    else:
        nombreEssais += 1
        nombreEssaisRestant = 10 - nombreEssais
        print('La lettre n\'est pas dans le mot, il vous reste ', nombreEssaisRestant, ' essais \n')


# Lorsqu'une lettre est trouvée, l'afficher dans le mot


