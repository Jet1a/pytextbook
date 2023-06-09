h = int(input("Enter high -> "))
w = int(input("Enter width -> "))

for row in range(h):
   
    for column in range(w):

        if row == 0 or row == h-1 or column == 0 or column == w-1 :
            print("x",end="")
        else:
            print(" ",end="")
    
    print(" ")
# output
# Enter high -> 5
# Enter width -> 5
# xxxxx
# x   x
# x   x
# x   x
# xxxxx