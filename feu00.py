import sys

def def_rectangle(long,height):
    table = [[" " for i in range(long)] for j in range(height)]
    
    for i in range(long):
        table[0][i] = table[height-1][i] = "-"
        
    for i in range(height):
        table[i][0] = table[i][-1] = "|"
        
    table = corner(table,height)
    
    return table

def corner(rectangle,height):
    
    for i in range(0,-2,-1):
        rectangle[0][i] = "O"
        rectangle[height-1][i] = "O"
        
    return rectangle

if __name__ == "__main__":
    long = int(sys.argv[1])
    height = int(sys.argv[2])
    rectangle = def_rectangle(long,height)
    
    for i in range(height):
        print("".join(rectangle[i]))
