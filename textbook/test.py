print("Hello World") # welcome to my textbook

#everything in wrong order to learn :D

a = int(input("First : "))
b = float(input("Second : "))

print(a+b)

# int = real number %d
# float = decimal %f
# string = text %s
# bool (boolean) = T,F
# Lists = []
# == เท่ากับ " = " = กำหนดตัวแปร
# if ---> elif ---> else
# while loop = ทำจนกว่าจะ false

i = 1
while i <= 5:
    print(i)
    i += 1

# for loop คำสั่งวนซ้ำตามรอบแน่นอน

for k in range(10): #(start,stop,step)
    print(k)

for k in range(1,10,1): #(start,stop,step)
    print(k)

# functions = def functions name():

def hola():
    print("Hola")

hola()

def sum_fun(a,b): #ไม่มีการคืนค่า
    sum = a+b
    print(sum)

sum_fun(5,10)

def sum_fun(a,b): #มีการคืนค่า มีพารามีเตอร์ (a,b) ในวงเล็บคือพารามีเตอร์
    sum = a+b
    return sum
a = sum_fun(5,10)

n = a + 20
print(n)

def sum_fun(): #มีการคืนค่า ไม่มีพารามีเตอร์
    sum = 20+20
    return sum
a = sum_fun()

n = a + 20
print(n)

side = int(input())
high = int(input())

def square_area():
    if side <= 0 or high <= 0:
        return "Error"
    area = side * high
    return area

total = square_area()

print(total)

# x!=y ไม่เท่ากับ

#Compound Assignment

x=10
print('Before',x)
x += 10 # x = x + 10
x -= 5 # x = x - 5
print('After',x)

#Ternary Operator

age = int(input('Enter your age: '))

print('Teen') if age>=15 else print('Kid')

# if ซ้อน if

age = input("Enter your age:")

if age<=15:
    if age == 15:
        print('Junior')
    elif age == 14:
        print('M.2')
else :
    print('Senior')

#While Loop

""""
while expresssion :
    statement  
"""

i = 0
while i < 10:
    print("Hello")
    i += 1

# For loop

# for i in range (start,stop,step) #กำหนดรอบ

for i in range(3): # 0,1,2
    print("Round = ",i,"Hello World")

# For loop loop

i  = 1
while i <= 3 :
    j = 1
    while j<=5:
        print("Round = ",i,"Position = ", j)
        j += 1
    i+=1 #ทำข้างในจนกว่าจะเท็จ ส่งต่อมาทำข้างนอก

for i in range(1,4):
    print("Round =",i)
    for j in range(1,6):
        print("Position =",j)

# Break / Continue

i = 1
while i <= 10:
    print(i)
    if(i==5):
        break #กระโดดออกจากลูปทันที
    i+=1
else:
    print("Finished")

i = 0
while i <= 10:
    i+=1
    if(i==5):
        continue #กระโดดข้ามเมื่อเท่ากับ 5 แล้วทำงานต่อ
    print(i)
else:
    print("Finished")
