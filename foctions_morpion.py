from random import randint


def affichage(tab):
    '''Affiche la grille de morpion donnée comme entrée. '''

    grille = [[0] * 3 for loop in range(3)]

    for loop in range(3):
        a = loop
        for unloop in range(3):
            b = unloop
            c = "|"
            d = " "
            if tab[a][b] == "i" or tab[a][b] == None:
                tab[a][b] = " "
            grille[a][b] = c + d + tab[a][b]

    for loop in range(3):
        a = grille[loop]
        for unloop in range(3):
            b = a[unloop]
            print(b, end=" ")
        print("|")



def nouvelle_partie():
    '''Demande à quel type de partie le joueur veux jouer et renvoie le nombre de manches gagnantes qu'il faut avoir pour gagner la partie.'''

    end = int(input("A quel type de partie voulez-vous jouer ?\n1 = bo 1\n3 = bo 3\n5 = bo 5\n7 = bo 7\n10 = nombre de round illimité\n"))
    if end < 9:
        return end // 2 + 1
    elif end == 10:
        return 100000000000000000000000000
    else:
        print("Cela n'existe pas, nous devons appeler la BAP")
        exit()

def coup(tab, x, y, j, IA):
    ''' Permet de mettre le coup joué par un joueur au bon endroit de la grille. A besoin  du tableau actuel de la partie, du coup joué et du joueur. Renvoi le tableau actualisé comme sortie. '''

    x -= 1
    y -= 1
    if x > 2 or y > 2:
        if not IA:
            print("Ce coup n'est pas valable, veuillez refaire votre coup.")
            x = int(input(""))
            y = int(input(""))
        else:
            x = randint(1,3)
            y = randint(1, 3)
        return coup(tab, x, y, j, IA)
  
    elif tab[x][y] != " ":
        if not IA:
            print("Cette case est déjà occupée, veuillez rejouer.")
            x = int(input(""))
            y = int(input(""))
        else:
            x = randint(1,3)
            y = randint(1, 3)
        return coup(tab, x, y, j, IA)
    
    elif j:
        tab[x][y] = "X"
    else:
        tab[x][y] = "O"
 
    return tab


def tableau_rempli(tab):
    """Prend la grille de morpion comme entrée et renvoi True si elle est pleine et False si l'inverse."""
    a = False
    for loop in range(3):
        for unloop in range(3):
            if tab[loop][unloop] == " ":
                a = True
    return a

def victoire(tab):
    """Prends comme entrée la grille de morpion. Renvoi True si trois meme symboles sont aligné et False si ce n'est pas le cas."""
    for loop in range(3):
        a = 0
        b = tab[loop][0]
        for unloop in range(3):
            if tab[loop][unloop] == b:
                a += 1
        if a == 3 and b != " ":
            return True
    
    for loop in range(3):
        a = 0
        b = tab[0][loop]
        for unloop in range(3):
            if tab[unloop][loop] == b:
                a += 1
        if a == 3 and b != " ":
            return True

    if tab[0][0] == tab[1][1] and tab[0][0] == tab[2][2] and tab[0][0] != " ":
        return True
    
   
    if tab[2][0] == tab[1][1] and tab[1][1] == tab[0][2] and tab[2][0] != " ":
        return True
    
    return False

def coup_IA(tab):
    """Prend comme entrée la grille de morpion et renvoi les coordonnées x et y du meilleur coup possible pour l'IA(depth = 1)"""
    
    x_p = randint(1, 3)
    y_p = randint(1, 3)
    for loop in range(3):
        a = tab[loop][0]
        b = tab[loop][1]
        c = tab[loop][2]
        if a != " " or b != " ":    
            if a == b and a == "O" and c == " ":
                return loop + 1, 3
    
            if a == c and a == "O" and b == " ":
                return loop + 1, 2
    
            if b == c and b == "O" and a == " ":
                return loop + 1, 1
    
            if a == b and a == "X" and c == " ":
                x_p=  loop + 1
                y_p = 3
    
            if a == c and c == "X"and b == " ":
                x_p =  loop + 1
                y_p = 2
    
            if b == c and b == "x" and a == " " :
                x_p =  loop + 1
                y_p = 1
    
    for loop in range(3):
        a = tab[0][loop]
        b = tab[1][loop]
        c = tab[2][loop]
        if a != " " or b != " ": 
            if a == b and a == "O" and c == " ":
                return 3, loop + 1
    
            if a == c and a == "O" and b == " ":
                return 2, loop + 1
    
            if b == c and b == "O" and a == " ":
                return 1, loop + 1
    
            if a == b and a == "X" and c == " ":
                y_p=  loop + 1
                x_p = 3
    
            if a == c and c == "X" and b  == " ":
                y_p =  loop + 1
                x_p = 2
    
            if b == c and b == "x" and a  == " ":
                y_p =  loop + 1
                x_p = 1

    
    
    a = tab[0][0] 
    b = tab[1][1] 
    c = tab[2][2] 
    if a != " " or b != " ":
        if a == b and a == "O" and c  == " ":
            return 3, 3

        if a == c and a == "O" and b  == " ":
            return 2, 2

        if b == c and b == "O" and a  == " ":
            return 1, 1

        if a == b and a == "X" and c == " ":
            x_p=  3
            y_p = 3

        if a == c and c == "X" and b == " ":
            x_p = 2
            y_p = 2

        if b == c and b == "x" and a == " ":
            x_p = 1
            y_p = 1
        
    
    a = tab[0][2] 
    b = tab[1][1] 
    c = tab[2][0] 
    if a != " " or b != " ":
        if a == b and a == "O" and c == " ":
            return 3, 0

        if a == c and a == "O" and b == " ":
            return 2, 2

        if b == c and b == "O" and a == " ":
            return 1, 3

        if a == b and a == "X" and c == " ":
            x_p=  3
            y_p = 0

        if a == c and c == "X" and b == " ":
            x_p = 2
            y_p = 2

        if b == c and b == "x" and a == " ":
            x_p = 0
            y_p = 3
    
    return x_p, y_p
