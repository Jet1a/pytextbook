msg = ["aa","ab","ac","abc"]
sum = []
for i in msg:
    print(i,end=" ")
    sum.append(i.count("a"))
print(sum)