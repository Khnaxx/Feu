import sys


laby = []
with open("labyrinthe", "r") as l:
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
    exit

# combler les voix sans issues
def Display_no_issue(laby):
    presence_no_issue = 0
    while presence_no_issue != 4:
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

        presence_no_issue += 1
    
    return laby
laby = Display_no_issue(laby)

# Trouve le point de départ
def find_departure(laby):
    for i in range(len(laby)):
        for j in range(len(laby[0])):
            if laby[i][j] == "1":
                return [i,j]
# Trouve le point d'arrivée
def find_arrived(laby, depart):
    point_of_arrive = []
    for i in range(len(laby)):
        for j in range(len(laby[0])):
            if laby[i][j] == "2":
                point_of_arrive.append([i,j])
    proche = len(laby) * len(laby[0])
    for number, coordo in enumerate(point_of_arrive):
        if abs(int(str(depart[0]) + str(depart[1])) - int(str(coordo[0]) + str(coordo[1]))) < proche:
            proche = abs(int(str(depart[0]) + str(depart[1])) - int(str(coordo[0]) + str(coordo[1])))
            point = number
    return point_of_arrive[point]

depart = find_departure(laby)
arrived = find_arrived(laby,depart)

def display_finish(laby,depart):
    if laby[depart[0] + 1 ][depart[1]] == "2" or laby[depart[0]][depart[1] + 1] == "2" or laby[depart[0] - 1][depart[1]] == "2" or laby[depart[0]][depart[1] - 1] == "2":
        return True
    else: return False

def find_way(laby,depart,arrived,histo):
    if laby[depart[0] + 1 ][depart[1]] == " " and depart[0] + 1 <= arrived[0]: # Down
        depart[0] = depart[0] + 1
        histo = "D"
        return depart, histo  
    if laby[depart[0]][depart[1] + 1] == " " and depart[1] + 1 <= arrived[1]: # Right
        depart[1] = depart[1] + 1
        histo = "R"
        return depart, histo  
    if laby[depart[0] - 1][depart[1]] == " " and depart[0] - 1 >= arrived[0]: # Up
        depart[0] = depart[0] - 1
        histo = "U"
        return depart, histo  
    if laby[depart[0]][depart[1] - 1] == " " and depart[1] - 1 >= arrived[1]: # Left
        depart[1] = depart[1] - 1
        histo = "L"
        return depart, histo  
    if histo == "D":
        depart[0] = depart[0] + 1
        histo = "D"
        return depart, histo  
    elif histo == "R":
        depart[1] = depart[1] + 1
        histo = "R"
        return depart, histo  
    elif histo == "U":
        depart[0] = depart[0] - 1
        histo = "U"
        return depart, histo  
    elif histo == "L":
        depart[1] = depart[1] - 1
        histo = "L"
        return depart, histo     

i = 0
histo = ""
while True:
    if display_finish(laby,depart):
        print(information)
        for line in laby:
            print("".join(line))
        print(f"=> SORTIE ATTEINTE EN {i} COUPS !")
        break
    else:
        depart,histo = find_way(laby,depart,arrived,histo)
        laby[depart[0]][depart[1]] = "o"

        i += 1
