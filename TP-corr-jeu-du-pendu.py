





























import random

# Étape 1 : Définir une liste de mots possibles
mots = ["python", "ordinateur", "programme", "jeu", "pendu"]

# Étape 2 : Choisir un mot au hasard
mot_a_deviner = random.choice(mots)

# Étape 3 : Initialiser les variables du jeu
mot_cache = ["_"] * len(mot_a_deviner)  # Représentation du mot avec des underscores
lettres_essayees = []  # Liste des lettres déjà essayées par le joueur
essais_restants = 6  # Nombre d'erreurs autorisées

# Étape 4 : Boucle principale du jeu
while essais_restants > 0 and "_" in mot_cache:
    # Afficher l'état actuel du mot et les essais restants
    print("\nMot à deviner :", " ".join(mot_cache))
    print("Lettres essayées :", ", ".join(lettres_essayees))
    print(f"Essais restants : {essais_restants}")

    # Demander une lettre au joueur
    lettre = input("Proposez une lettre : ").lower()

    # Vérifier si la lettre a déjà été essayée
    if lettre in lettres_essayees:
        print("Vous avez déjà essayé cette lettre. Choisissez une autre.")
        continue

    # Ajouter la lettre à la liste des lettres essayées
    lettres_essayees.append(lettre)

    # Vérifier si la lettre est dans le mot à deviner
    if lettre in mot_a_deviner:
        print("Bonne lettre !")
        # Révéler la lettre dans le mot caché
        for index, char in enumerate(mot_a_deviner):
            if char == lettre:
                mot_cache[index] = lettre
    else:
        print("Mauvaise lettre...")
        essais_restants -= 1  # Réduire le nombre d'essais restants

# Étape 5 : Résultat du jeu
if "_" not in mot_cache:
    print("\nFélicitations ! Vous avez deviné le mot :", mot_a_deviner)
else:
    print("\nDommage ! Vous avez perdu.")
    print("Le mot à deviner était :", mot_a_deviner)
