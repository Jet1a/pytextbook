fruit = ["Mango","Melon","Banana"]
cost = [10,15,20]

for x,y in zip(fruit,cost): # zip จับคู่เลย
    print(x,y)
for x,y in zip(fruit,cost[::-1]): # zip จับคู่เลย กลับด้าน
    print("After",x,y)
