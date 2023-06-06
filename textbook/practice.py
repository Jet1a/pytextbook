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