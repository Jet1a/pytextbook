# Chess board
h = int(input("Enter high -> "))
w = int(input("Enter width -> "))

for row in range(w):
    for column in range(h):
        if (row + column)% 2 == 0:
            print("x",end="")
        else :
            print("o",end="")
    print("")

"""
print("x",end="") if(row + column)% 2 == 0 else print("o",end="")

"""

# 3 x 3
# row = 0 column = 0
# row = 0 column = 1
# row = 0 column = 2

# row = 1 column = 0
# row = 1 column = 1
# row = 1 column = 2