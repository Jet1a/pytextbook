number = [1,2,3,4,5]

print(number)
# Use len เพื่อหยิบออกมาใช้ทีละตัว

for n in range(len(number)):
    number[n] = number[n] ** 2
print(number)

# short Ver
number = [ n**2 for n in number]
print(number)