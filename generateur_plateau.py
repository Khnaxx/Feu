import sys
import random

x = int(sys.argv[1])
y = int(sys.argv[2])
density = int(sys.argv[3])

print(f"{x}.xo")

for i in range(0,x):
    for j in range(0,y):
        if (random.randint(0,y)*2 < density):
            print("x",end = "")
        else: print(".",end = "")
    print()
