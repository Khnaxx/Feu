import sys

plateau = []
with open(sys.argv[1], "r") as s:
    to_check = s.readline().rstrip()
    for line in s:
        plat = line.rstrip()
        plateau.append(plat)

full = to_check[-1]


# Vérifier la longueur des lignes et supprimer le 1er de la liste "plateau"

def check_argument(plateau,to_check):
    nb_line = int(to_check[0])
    caractere = to_check[1:3]
    if nb_line != len(plateau):
        return False
    long = len(plateau[0])
    for i in range(len(plateau)):
        if long != len(plateau[i]):
            return False
    string_plateau = ""
    for line in plateau:
        string_plateau += line
    for caract in string_plateau:
        if caract not in caractere:
            return False
    return True

if not check_argument(plateau,to_check):
    print("error")
    exit()


plateau = [[plateau[i][j] for j in range(len(plateau[0]))] for i in range(len(plateau))]

max_size = 0
origine_y = 0
origine_x = 0

def carre(plateau,deb_x,deb_y):
    size = 0
    while True:
        for i in range(size):
            for j in range(size):
                try:
                    if plateau[deb_y + i][deb_x + j] == "x":
                        return i,j,size-1
                except : return i,j,size-1
        size += 1
        
while origine_y < len(plateau) - max_size:
    yy, xx , size = carre(plateau,origine_x,origine_y)
    if size > max_size:
        UL_x = origine_x
        UL_y = origine_y
        max_size = size
    origine_x += 1
    if origine_x > len(plateau[0])-max_size:
        origine_x = 0
        origine_y += 1

for i in range(UL_y,UL_y+max_size):
    for j in range(UL_x,UL_x+max_size):
        plateau[i][j] = full

for line in plateau:
    print("".join(line))

        
