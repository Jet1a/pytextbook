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

#String Deep

name = "OpzTV" #index ตัวแรก เริ่มที่ => 0

# ช่องว่างในข้อความก็นับเป็น index

print (name[0:3]) #[เริ่ม:ก่อนถึงตัวจบ]
# จะได้ Op ถ้า จบที่ 4 จะได้ Opz

name = "OpzTV : 10" 
print(name[-2]) # จะนับจากหลัง จะได้ 1
print(name[-2:]) # จะนับต่อ จะได้ 10

name = " OpzTV"
print(len(name)) #นับ Index
name=name.strip() # Strip ลบช่องว่าง
print(len(name))

name = "OpzTV"
print(name.upper()) #ตัวพิมพ์ใหญ่
print(name.lower()) #ตัวพิมพ์เล็ก
print(name.capitalize()) #ตัวพิมพ์ใหญ่ตัวแรกสุดเท่านั้น

name = "OpzTV"
print(name.replace("Opz","Breakgate")) #แทนที่ [old,new,count] count หากมีซ้ำหลากอันแล้วอยากแทนแค่บางลำดับ
name = "OpzTV 3 3 3"
print(name.replace("3","5",2))

name = "OpzTV"
i = "TV" in name #เช็ค " " ในตัวแปรมั้ย จะได้ => true false
i = "TV" not in name
print(i)

fname = "Krit"
sname = "Banki"
age = "20"
fullname = fname + sname + age #ต่อstring
print(fullname,"\t789") #\t == tab

fname = "Krit"
sname = "Banki"
age = "20"
inc = 13659.455423
txt = "First name : {0}\tLast name : {1}\tage : {2} \tIncome :{3:.3f}" #เลขตามลำดับ
print(txt.format(fname,sname,age,inc)) #การใช้ format {}

name = "Mr.Chicken"
if name.startswith("Mr"): #check started word
    print("Male")
elif name.endswith("ed"): #check ended word
    print("Past")
else :
    print("Undefined")

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


#-------------Exercise------------------

def multi_sum(a,b):
    if a*b <= 1000:
        return a*b
    else:
        return a+b

print(multi_sum(30,30))    

#####################

previous_num = 0
for i in range (10):
    total_sum = previous_num + i
    print("Current Number", i, "Previous Number", previous_num, "Sum:", total_sum)

    previous_num = i

#################

word = input("Type word ")
print("Original word:", word)

size = len(word)

print("Even index char")
for i in range (0, size - 1,2):
    print("index[", i, "]", word[i])

###################

num_list = [10, 20, 33, 46, 55]
for num in num_list:
    if num % 5 == 0: # % หารเอาเศษ
        print(num)
        
#####################

str_x = "Emma is good developer. Emma is a writer"

count = str_x.count("Emma")
print(count)

#################

temp = input("Enter temperature (C,F) :")

degree = int(temp[:-1])
unit = temp[-1].upper()

if unit == "C":
    result = (degree * 9)/5 + 32 
    unitresult = "Falenhigh"
if unit == "F":
    result = (degree - 32)*5/9
    unitresult = "Celcius"

print("Temperature ",degree,"to",unitresult,'=', result)

#############

import tkinter as cal

def multi_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text="Zero be Zero")
        return

    output = ""
    for i in range (1,13):
        output += str(number) + ' x ' + str(i) + ' = ' + str(number * i) + '\n'
        #output += ' = ' + str(number * i) 

    output_label.configure(text=output)

window = cal.Tk()
window.title("Math Calculator")
window.minsize(800,800)

title_label = cal.Label(master=window, text="Multiple")
title_label.pack()

number_input = cal.Entry(master=window, width=30)
number_input.pack()

go_button = cal.Button(
    master=window, text="Equal to",
    command=multi_output, width=20, height=2
    )
go_button.pack()

output_label = cal.Label(master=window)
output_label.pack()

window.mainloop()