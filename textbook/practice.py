#-------------Exercise------------------

def multi_sum(a,b):
    if a*b <= 1000:
        return a*b
    else:
        return a+b

print(multi_sum(30,30))    

# Showing for range num with previous num and total sum

previous_num = 0
for i in range (10):
    total_sum = previous_num + i
    print("Current Number", i, "Previous Number", previous_num, "Sum:", total_sum)

    previous_num = i

# String len and print only index

word = input("Type word ")
print("Original word:", word)

size = len(word)

print("Even index char")
for i in range (0, size - 1,2):
    print("index[", i, "]", word[i])

# Find number in list % 5 == 0

num_list = [10, 20, 33, 46, 55]
for num in num_list:
    if num % 5 == 0: # % หารเอาเศษ
        print(num)
        
# Count string

str_x = "Emma is good developer. Emma is a writer"

count = str_x.count("Emma")
print(count)

# Find min max value

max,min = 0,0

while True :
    number = int(input("Enter your number :"))
    
    if number <0 :
        break
    if number >max:
        max = number
    if number < max :
        min = number

print("Most value is :", max)
print("Less value is :", min)

# Ladder Number

ended = int(input("Enter number : "))

for row in range (1,ended+1):
    for column in range (1, row + 1):
        print(column, end = " ") #end = " " แสดงแนวนอน
    print("") #เว้นแต่ละรอบ

# Print Square

number = int(input("Enter size : "))

for row in range(number):
    for col in range(number):
        print("*", end=" ") 
    print("")