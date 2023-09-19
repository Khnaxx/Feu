laby = []
with open("/Users/marcvanthuyne/Documents/GitHub/Feu/labyrinthe", "r") as l:
    for line in l:
        plat = line.rstrip()
        laby.append(plat)

information = laby[0]
del(laby[0])

laby = [[laby[i][j] for j in range(len(laby[0]))] for i in range(len(laby))]

def check_enter(laby,information): # Verification if information is in laby
    # Data
    caract_full = information[information.index(" ")-1]
    nb_line = int(information[0:information.index("x")])
    nb_column = int(information[information.index("x")+1:information.index(caract_full)])
    departure = information[-3]
    arrive = information[-2]

    if nb_line != len(laby): # Check the number of line
        return False

    for i in range(nb_line): #Check the number of column
        if len(laby[i]) != nb_column + 1: 
            return False
    nb_caract_full = 0
    for i in range(nb_line): # Check if caract_full is in the list laby
        nb_caract_full += laby[i].count(caract_full)
    if nb_caract_full == 0 or nb_caract_full == nb_line * nb_column:
        return False
    
    i = 0 
    for line in laby: # Check if departure and arrive is in list
        if departure or arrive in line:
            i += 1
            if i == 2:
                return True
    return False

if not check_enter(laby,information):
    print("error")

# combler les voix sans issues
def Display_no_issue(laby):
    for i in range(len(laby)):
        for j in range(len(laby[0])):
            if laby[i][j] == " ":
                nb_issue = 0
                if j-1 >= 0:
                    if laby[i][j-1] == "*":
                        nb_issue += 1
                if i-1 >= 0:
                    if laby[i-1][j] == "*":
                        nb_issue += 1
                if j+1 < len(laby[0]):
                    if laby[i][j+1] == "*":
                        nb_issue += 1
                if i+1 < len(laby):
                    if laby[i+1][j] == "*":
                        nb_issue += 1
                if nb_issue == 3:
                    laby[i][j] = "*"
    
    return laby

laby = Display_no_issue(laby)

# Trouve le départ 1
depart = []

def find_departure(laby):
    for i in range(len(laby)):
        for j in range(len(laby[0])):
            if laby[i][j] == "1":
                return [i,j]

depart = find_departure(laby)

# Checker dans quel direction
first_way = []
second_way = []
new_place = depart.copy()

def display_deplacement_clockwise(labyrinthe,depart):
    if labyrinthe[depart[0]][depart[1]-1] == " " and depart[1]-1 >= 0:
        return "Left" , [0,-1]
    elif labyrinthe[depart[0]-1][depart[1]] == " " and depart[0]-1 >= 0:
        return "Up" , [-1,0]
    elif labyrinthe[depart[0]][depart[1]+1] == " " and depart[1]+1 <= len(laby[0]):
        return "Right" , [0,1]
    elif labyrinthe[depart[0]+1][depart[1]] == " " and depart[0]+1 <= len(laby):
        return "Down" , [1,0]

def check_arrive_near(laby,depart):
    if labyrinthe[depart[0]][depart[1]-1] == "2" and depart[1]-1 >= 0:
        return True
    elif labyrinthe[depart[0]-1][depart[1]] == "2" and depart[0]-1 >= 0:
        return True
    elif labyrinthe[depart[0]][depart[1]+1] == "2" and depart[1]+1 <= len(labyrinthe[0]):
        return True
    elif labyrinthe[depart[0]+1][depart[1]] == "2" and depart[0]+1 <= len(labyrinthe):
        return True
    else:
        return False

def display_deplacement_conterclockwise(labyrinthe,depart):
    if labyrinthe[depart[0]+1][depart[1]] == " " and depart[0]+1 <= len(labyrinthe):
        return "Down" , [1,0]
    elif labyrinthe[depart[0]][depart[1]+1] == " " and depart[1]+1 <= len(labyrinthe[0]):
        return "Right" , [0,1]
    elif labyrinthe[depart[0]-1][depart[1]] == " " and depart[0]-1 >= 0:
        return "Up" , [-1,0]
    elif labyrinthe[depart[0]][depart[1]-1] == " " and depart[1]-1 >= 0:
        return "Left" , [0,-1]

clockwise = True
labyrinthe = laby.copy()
i = 0
while i != 17:
    if check_arrive_near(labyrinthe,new_place):
        if clockwise:
            clockwise = False
            labyrinthe = laby.copy()
            new_place = depart
            print(first_way)
            print(second_way)
            print(new_place)
        else: # controler le vainqueur
            print("fini, reste à comparer")
            break

    if clockwise:
        direction , coordo = display_deplacement_clockwise(labyrinthe,new_place)
        first_way.append(direction)
    else:
        direction , coordo = display_deplacement_conterclockwise(labyrinthe,new_place)
        second_way.append(direction)

    new_place = [new_place[i] + coordo[i] for i in range(2)]
    labyrinthe[new_place[0]][new_place[1]] = "o"

    for i in range(len(laby)):
        print("".join(labyrinthe[i]),"".join(laby[i]))

    i +=1
    
print("sortie")
for line in laby:
    print("".join(line))