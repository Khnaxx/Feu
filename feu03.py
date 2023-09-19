import sys

sudoku = []
with open(sys.argv[1], "r") as s:
    for line in s:
        sudos = line.rstrip()
        sudoku.append(sudos)

def Fill_horizontal(sudoku):
    for i in range(9):
        if sudoku[i].count(".") == 1:
            for j in range(1,10):
                if str(j) not in sudoku[i]:
                    sudoku[i] = sudoku[i].replace(".", str(j),1)
                    break
    return sudoku

def Fill_vertical(sudoku):
    for i in range(9):
        check_vertical = []
        for j in range(9):
            check_vertical.append(sudoku[j][i])
        if "." in check_vertical:
            for j in range(1,10):
                if str(j) not in check_vertical:
                    index = check_vertical.index(".")
                    sudoku[index] = sudoku[index].replace(".", str(j),1)
    
    return sudoku

sudoku = Fill_horizontal(sudoku)
sudoku = Fill_vertical(sudoku)
for line in sudoku:
    print(line)
