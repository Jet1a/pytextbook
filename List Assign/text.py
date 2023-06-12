name = []
getname = str(input("Enter your file name : "))
getname.strip()
name.append(str(getname))
print("Your files name",name)
name = str(name)
file,typ = name.split(".")
print("Your file name -> ",file[2:])
print("Your file type -> ",typ[:-2])