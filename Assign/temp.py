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