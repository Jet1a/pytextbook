guest = ["Andy","Mark","John","Cindy","Lyla"]

print("Before sort: ",guest)
guest.append("Peter")
guest.sort()
print("After sort:",guest)
guest.reverse()
print("After reverse sort:",guest)
guest = guest[::-1]
print("After sort:",guest)