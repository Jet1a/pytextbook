# Tuples
tup = (1,2,3,4,"stringok",False,3.14) #tuple ()
lis = [1,2,3,4,"stringok",False,3.14] #list []

## change tuple to list

lis = list(tup)
lis[0] = "Yippee"
print("Before :",tup)
tup = tuple(lis)
print("After :",tup)

## if loop
if "stringok" in tup:
    print("Ya it is")
else :
    print("Nah")

## len with loop

for item in range(len(tup)):
    print(tup[item])

## join tuples (tuple can only join with tuple) !

old = ("Corgi",60)
new = ("Pug")
    ### groupnew = old + new
    ### new += old
groupnew = old + (new,)
print(groupnew)

### join tuple with list

fruits = ("Apple","Banana","Orange")
fish = ["Salmon","Koi","Bass"]

fruits += tuple(fish) ### Change list into tuple
print(fruits)

### Del tuple

""" 
del Fish
print(fish) ## Del all  """

newfish = list(fish)
print("Before > ",fish)
 # fish.pop() # Del lastest #
fish.remove("Salmon") # Del specific
print("After > ",fish)
newfish = tuple(fish) # Back to tuple

### count tuple & index

b = fruits.count("Banana")
print ("Banana count >> ",b)

p = fruits.index("Banana") ### find position index.()
print("Found position >>",p)

### Sort tuple
value = (21,5,42,95,31,19,0,4,74,23,45)
print("Before Sort :",value)
listvalue = list(value)
listvalue.sort() ## Sort -->
value = tuple(listvalue)
print("After Sort :",value)
listvalue.reverse() ## Reverse sort <---
value = tuple(listvalue)
print("Reverse Sort :",value)

## put tuple --> variable

ks = (10,20,30) ## ks(in order)
a,b,c = ks
print(a,b,c)

## Swap tuple

u = ("html","css")
i = ("C++","Java")
print(" u Before ",u)
u,i = i,u
print(" u After ",u)

## tuple --> str

character = ("Alpha","Beta")
strname="".join(character) # "" change to str
print(type(strname))

## reversed tuple

s = ("Heat","Cold",50,100,0)
y = reversed(s)
print(tuple(y))