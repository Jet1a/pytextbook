"""
จัดกลุ่มข้อความพฐ.
List = [] , ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้ , ซ้ำกันได้ , ซ้ายไปขวา
Tuple = () , ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลไม่ได้ , ซ้ำกันได้ , ซ้ายไปขวา
Set = {} , ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้ , ซ้ำกันไม่ได้ , ลำดับไม่แน่นอน
"""
# Set

veggie = {"Carrot","Cabbage","Pumpkin"}
print(veggie) # output will not in order

# Constructor
pet = set(["Cat","Dog"]) #ข้อมูลที่ซ้ำจะไม่แสดงผล
print(pet)

# add
pet.add("Fish") #ลบตัวเดียว
# update
pet.update(["Tiger","Horse","Bird"]) #หลายตัว

# remove
pet.remove("Cat") #ลบตัวเดียว ถ้าไม่เจอจะ Error
# discard
pet.discard("Cat") #ลบตัวเดียว ถ้าไม่เจอก็จะไม่ Error

# loop
for animal in pet:
    print("Info :",animal)

# len
print(len(pet))

# if
if "Cat" in pet:
    print("Meow")
else:
    print("No")

# in , not
print("Cat" in pet) # output (True,Flase)

## Set Operation
""" 
fruitA = {"Banana","Pineapple","Peach"}
fruitB = {"Kiwi","Watermelon","Melon"} 
# union
mixFruit = fruitA.union(fruitB) #can also use update fruitA.update(fruitB)
print(mixFruit)
"""
#
fruitA = {"Banana","Pineapple","Peach","Kiwi","Watermelon"}
fruitB = {"Kiwi","Watermelon","Melon","Banana"} 
## เอาตัวที่มีใน B ออกจาก A สลับได้
fruitC = fruitA.difference(fruitB) 
print(fruitC)
## เอาตัวที่เหมือกัน
fruitD = fruitA.intersection(fruitB)
print(fruitD)

print(fruitA)
fruitA.difference_update(fruitB) #เอากลับไปใส่ใน A
print(fruitA)

#subset , superset
supset = {1,2,3,4,5,6}
subset = {1,2,3}
print(supset.issuperset(subset))
print(subset.issubset(supset))

# Frozen set (fix set)
fish = frozenset(["Salmon","Koi"])
# cant add & cant discard

##end