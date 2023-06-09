number = []
odd = []
even = []
while True:
    n = int(input("Enter number : "))
    if n < 0:
        break
    if n % 2 == 0:
        even.append(n)
    else :
        odd.append(n)
    number.append(n)
print(number)
print("Odd",odd)
print("Even",even)