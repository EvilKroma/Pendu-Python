
# Jeu du pendu - Python 🐍

L'objectif est d'écrire un programme en Python qui permet de jouer au jeu du pendu.  
Le programme doit choisir un mot au hasard dans une liste prédéfinie, puis demander au joueur de deviner les lettres de ce mot.  
Le joueur a un nombre limité d’essais pour trouver le mot. Si le joueur dépasse ce nombre sans avoir trouvé le mot, il perd.

## Règles

Une liste de mots est prédéfinie dans le programme.  
Le mot à deviner est choisi aléatoirement.  
Le programme masque le mot en remplaçant chaque lettre par un underscore (_).

## A chaque itération

Le joueur propose une lettre.  
Si la lettre est correcte, elle est révélée dans le mot.  
Si la lettre est incorrecte, le nombre d’essais restants diminue.  

Le jeu se termine lorsque :  
Le joueur a deviné toutes les lettres du mot (victoire).  
Le joueur a utilisé tous ses essais sans trouver le mot (défaite).  
