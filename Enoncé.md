# TP : Jeu du pendu
# -----------------------------------
# Objectif : Écrire un programme en Python qui permet de jouer au jeu du pendu. Le programme doit choisir un mot au hasard dans une liste prédéfinie, puis demander au joueur de deviner les lettres de ce mot. Le joueur a un nombre limité d’essais pour trouver le mot. Si le joueur dépasse ce nombre sans avoir trouvé le mot, il perd.

# Règles :

# Une liste de mots est prédéfinie dans le programme.
# Le mot à deviner est choisi aléatoirement.
# Le programme masque le mot en remplaçant chaque lettre par un underscore (_).

# À chaque tour :
# Le joueur propose une lettre.
# Si la lettre est correcte, elle est révélée dans le mot.
# Si la lettre est incorrecte, le nombre d’essais restants diminue.
# Le jeu se termine lorsque :
# Le joueur a deviné toutes les lettres du mot (victoire).
# Le joueur a utilisé tous ses essais sans trouver le mot (défaite).




# Quelques indices
# ----------------

# (Il est possible que vous ayez besoin de import random pour aller choisir un mot au hasard dans la liste de mots que vous proposerez à votre joueur.)

# Algorithme simplifié :

# Initialisation :

# Créer une liste de mots possibles.
# Choisir un mot au hasard.
# Initialiser une variable pour stocker les essais restants.
# Préparer une liste de lettres déjà devinées.
# Boucle principale :

# Tant que le joueur a des essais restants et que le mot n’est pas complètement deviné :
# Afficher le mot masqué avec les lettres trouvées.
# Afficher les lettres déjà essayées et le nombre d’essais restants.
# Demander au joueur une lettre.
# Si la lettre a déjà été essayée, afficher un message.
# Sinon :
# Ajouter la lettre aux lettres essayées.
# Si la lettre est dans le mot :
# Révéler la lettre dans le mot masqué.
# Sinon :
# Réduire le nombre d’essais restants.
# Fin du jeu :

# Si le mot est deviné, afficher un message de victoire.
# Sinon, afficher un message de défaite et révéler le mot.