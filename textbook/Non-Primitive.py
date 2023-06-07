# Lists Deep

number = [] # empty list
number = [1,2,3,4,5] #  5 member in list
name = ["Gwen","Peter"]
all = [10,"Mr.Egg",True,3.14,-10]

## constructor

name = list(["Gwen","Peter","Penny"])

## specific list

print(all[0],number[2],name[1],all[-2])
print(">",name[0],name[2])
print(">>",all[1:4],number[-5])

## chage info

"""" print("Before :",name)
name[2] = "Parker" #variable[index] = " "
print("After :",name) """

## use for loop

sum = 0
for item in number:
    sum += item
print("Value",sum)

## list check eiei

weapon = ["sword","bow","axe","bomb"]

if "bow" in weapon:
    print("Yes")
else :
    if "bomb":
        print("Run boi Runnn")
    else :
        print("Nothing here")

## len list

print(len(weapon))
for gear in range(len(weapon)):
    print(weapon[gear])

## add list

### append add new info from last
weapon.append("wand")
weapon.append("spear")
### insert add new info from specific index
print("Before :",weapon)
weapon.insert(2,"claw")
print("After :",weapon)

## remove list

### remove
weapon.remove("bomb")
### pop (remove lastest added info)
weapon.pop()
### del (specific index)
#del " " deleted list and info
del weapon[0]
print("Del :",weapon)
weapon.clear() # clear only info in list
print("Clear :",weapon)

## copy list

x = []
print(x)
x = name.copy()
print(x)

## merge list

allGroup = name + number

number.extend(name) #extend add with no need new variable
print(number)

## count list
### count how many .count() in list
number = [1,2,3,4,5,4,4]
n = number.count(4)
print(n)

# Tuples







# Sets






#Dict





