greet = ["Hello ","Hi ","Ayo ","See ya "]
person = ["Pete","Gwen","Penny"]
result = []
# Formal

for n in greet:
    for p in person:
        result.append(n + p)
print(result)

result =[n+p for n in greet for p in person]