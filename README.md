# Solveur de Sudoku en Python
## 🧩 Règles du Sudoku
**Le Sudoku est un jeu de réflexion qui se joue sur une grille de 9x9 cases, divisée en neuf sous-blocs de 3x3.**

Le but est de remplir la grille avec des chiffres de 1 à 9 en respectant les contraintes suivantes :
- Chaque ligne doit contenir tous les chiffres de 1 à 9, sans répétition.
- Chaque colonne doit contenir tous les chiffres de 1 à 9, sans répétition.
- Chaque bloc 3x3 doit contenir tous les chiffres de 1 à 9, sans répétition.

Une grille de départ propose certains chiffres déjà placés ; le reste des cases doit être complété par le joueur (ou le programme !).

## ⚙️ Fonctionnement du programme
**Ce programme résout n'importe quelle grille de Sudoku valide en utilisant un algorithme de backtracking (retour sur trace).**

Voici comment il fonctionne, étape par étape :
### 1. Recherche de la solution (fonction principale)
```python
solution_sudoku(grille)
```
Cette fonction prend en entrée une grille de Sudoku sous forme de liste de listes (9x9), où les cases vides sont représentées par des 0.<br>
Elle appelle une fonction interne de backtracking pour remplir la grille.
### 2. Backtracking (fonction récursive)
```python
def backtracking(i, j):
    ...
```
*Parcourt la grille case par case.<br>
Si une case est déjà remplie,<br>
passe à la suivante.<br>
Sinon,<br>
essaie chaque chiffre possible (de 1 à 9) :<br>
Vérifie si le chiffre respecte toutes les contraintes du Sudoku (ligne, colonne, bloc).<br>
Si oui,<br>
place le chiffre et continue la résolution.<br>
Si une impasse est atteinte,<br>
efface la case (remet à 0) et essaie une autre valeur.*
### 3. Vérification des contraintes
Trois fonctions vérifient si un chiffre peut être placé :
#### Bloc 3x3 :
```python
val_possible_dans_bloc(L, i, j, val)
```
*Vérifie que le chiffre val n’est pas déjà présent dans le bloc 3x3 correspondant à la case (i, j).*
#### Ligne :
```python
val_possible_sur_ligne(L, i, val)
```
*Vérifie que val n’est pas déjà présent sur la ligne i.*
#### Colonne :
```python
val_possible_sur_colonne(L, j, val)
```
*Vérifie que val n’est pas déjà présent sur la colonne j.*
### 4. Passage à la case suivante
```python
case_suivante(i, j)
```
*Calcule la position de la prochaine case à traiter (passe à la colonne suivante, ou à la ligne suivante en fin de ligne).*
### 5. Affichage de la grille
```python
afficher_grille(grille)
```
*Affiche la grille résolue de manière lisible, sans crochets ni virgules, avec un alignement parfait pour chaque ligne.*
## ✨ Exemple d’utilisation
```python
grille = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

solution_sudoku(grille)
afficher_grille(grille)
```
### Affichage obtenu :
```text
 5  3  4  6  7  8  9  1  2
 6  7  2  1  9  5  3  4  8
 1  9  8  3  4  2  5  6  7
 8  5  9  7  6  1  4  2  3
 4  2  6  8  5  3  7  9  1
 7  1  3  9  2  4  8  5  6
 9  6  1  5  3  7  2  8  4
 2  8  7  4  1  9  6  3  5
 3  4  5  2  8  6  1  7  9
```
## 📄 Remarques
Le programme suppose que la grille fournie est valide et possède une solution unique.

Pour toute question ou suggestion, n’hésitez pas à ouvrir une issue ou à proposer une pull request !

Bon Sudoku ! 🧠
