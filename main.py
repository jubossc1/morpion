from fonctions import *
import os

clear = lambda: os.system('clear')
print("Bienvenue !")

j1 = input("Quel est le nom du premier joueur ?\n")
J1 = True
J2 = False
j1_point = 0
nb_joueur  = input("Entrez '1' si vous voulez jouer contre l'ordinateur et '2' si vous voulez faire un match entre 2 personnes.\n")
if nb_joueur == "1":
    IA = True
    j2 = "l'ordinateur"
elif nb_joueur == "2":
    IA = False
    j2 = input("Quel est le nom du second joueur ?\n")
else:
    print("Ce mode n'existe pas, nous devons appeler la BAP")
    exit()

j2_point = 0
max_points = nouvelle_partie()
end = False

while True:
    clear()
    grille = [[" "] * 3 for loop in range(3)]
    while not end:
        # print(grille)
        affichage(grille)
        print(f"Au tour de {j1}")
        x = int(input("Sur quelle ligne voulez-vous placer votre croix ?\n"))
        y = int(input("Sur quelle colonne ?\n"))
        grille = coup(grille, x, y, J1, False)
        clear()
        if not tableau_rempli(grille):
            c = 13
            break
        if victoire(grille):
            c = 11
            break
    
        # print(grille)
        affichage(grille)
        print(f"Au tour de {j2}")
        if not IA:
            x = int(input("Sur quelle ligne voulez-vous placer votre croix ?\n"))
            y = int(input("Sur quelle colonne ?\n"))
        else:
            x, y = coup_IA(grille)
        
        grille = coup(grille, x, y, J2, IA)
        clear()
    
        if not tableau_rempli(grille):
            c = 13
            break
    
        if victoire(grille):
            c = 12
            break
    
    if c == 13:
        affichage(grille)
        print(
            "La grille de morpion est remplie, vous avez fait une égalité."
        )
    
    if c == 12:
        affichage(grille)
        j2_point += 1
        print(f"{j2} a gagné la partie.")
    
    if c == 11:
        j1_point += 1
        affichage(grille)
        print(f"{j1} a gagné la partie")

    print(f"{j1} à {j1_point} points et {j2} à {j2_point} points.")

    if j1_point == max_points:
        print(f"{j1} à gagné la partie")
        break

    if j2_point == max_points:
        print(f"{j2} à gagné la partie")
        break
