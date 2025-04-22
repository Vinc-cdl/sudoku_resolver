# Vérifie si le chiffre n'est pas déjà présent dans le bloc
def val_possible_dans_bloc(L, i, j, val):
    bloc_i = (i // 3) * 3
    bloc_j = (j // 3) * 3
    for x in range(bloc_i, bloc_i + 3):
        for y in range(bloc_j, bloc_j + 3):
            if L[x][y] == val:
                return False
    return True


# Vérifie si le chiffre n'est pas déjà présent dans la ligne
def val_possible_sur_ligne(L, i, val):
    return val not in L[i]


# Vérifie si le chiffre n'est pas déjà présent dans la colonne
def val_possible_sur_colonne(L, j, val):
    for x in range(9):
        if L[x][j] == val:
            return False
    return True


# Passage à la case suivante. Va de gauche à droite puis passe à la ligne suivante.
def case_suivante(i, j):
    if j == 8:
        return i + 1, 0
    else:
        return i, j + 1


# Fonction principale qui prend la grille en argument et la ressort complétée
def solution_sudoku(L):
    def backtracking(i, j):
        if i == 9:
            return True
        if L[i][j] != 0:
            ni, nj = case_suivante(i, j)
            return backtracking(ni, nj)
        for val in range(1, 10):
            if (val_possible_dans_bloc(L, i, j, val) and
                    val_possible_sur_ligne(L, i, val) and
                    val_possible_sur_colonne(L, j, val)):
                L[i][j] = val
                ni, nj = case_suivante(i, j)
                if backtracking(ni, nj):
                    return True
                L[i][j] = 0
        return False

    backtracking(0, 0)
    return L


# Affiche la grille de manière propre, sans les virgule, sans les crochets, avec un espace entre chaque chiffre et un passage à la ligne entre chaque rangée
def afficher_grille(L):
    for ligne in L:
        print(' '.join(f"{val:2d}" for val in ligne))


# Mettez votre grille ici, celle-ci sert d'exemple, les espace après chaque virgule et les passage à la ligne après chaque liste ne sont pas obligatoires.
grille = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solution_sudoku(grille)
afficher_grille(grille)
