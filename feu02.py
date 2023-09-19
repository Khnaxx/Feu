import sys

# fichier source
with open(sys.argv[1],"r") as b:
    board = b.read().split("\n")
b.close()

# fichier to_find
with open(sys.argv[2],"r") as t:
    to_find = t.read().split("\n")
t.close()

def display_find_element(board,to_find):
    for Y in range(len(board)-len(to_find) + 1):
        for X in range(len(board[0])-len(to_find[0]) + 1):
            if board[Y][X] == to_find[0][0]:
                check = 0
                for y in range(len(to_find)):
                    for x in range(len(to_find[0])):
                        if board[Y+y][X+x] == to_find[y][x]:
                            check += 1
                        elif to_find[y][x] == " ":
                            check += 1
                        if check == len(to_find) + len(to_find[0]):
                            return Y, X
    else:
        print("Introuvable")
        quit()

def retour(board,to_find,coordo_Y, coordo_X):
    liste = [["-" for i in range(len(board[0]))] for j in range(len(board))]
    for i in range(len(to_find)):
        for j in range(len(to_find[0])):
            if to_find[i][j] == " ":
                continue
            else: liste[coordo_Y + i][coordo_X + j] = to_find[i][j]
    return liste


coordo_Y, coordo_X = display_find_element(board,to_find)
liste = retour(board,to_find,coordo_Y, coordo_X)
print("Trouvé !")
print(f"Coordonnées : {coordo_Y},{coordo_X}")
for line in liste:
    print("".join(line))
