
arr = []

while True:
    x = int(input("Enter number -> "))
    if x < 0 :
        break
    arr.append(x) #ต่อท้าย
    arr.sort() #only int
    
print(arr,"\n"+"Max value :",max(arr))
print("Min value :",min(arr))
print("Sum value :",sum(arr))

print("<End>")