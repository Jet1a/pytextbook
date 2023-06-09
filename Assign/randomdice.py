import random

#random number
myrandom = random.randrange(1,10) # 1 - 9
attempts = 3
while True:
    number = int(input("Enter answer : "))
    if number < 0:
        break
    if number == myrandom:
        print("Correct!! the correct number is :",myrandom)
        break
    else : 
        attempts -= 1
        if number < myrandom:
            print("Your answer is less than the answer. Try again","Attempts left >",attempts)
        elif number > myrandom:
            print("Your answer is more than the answer. Try again","Attempts left >",attempts)
    if attempts <= 0:
        print("You Lose","Correct number is",myrandom, "Start Again?")
        k = str(input())
        if k == 'Yes':
            attempts = 3
            continue
        else:
            print("Thank for playing :D")
            break