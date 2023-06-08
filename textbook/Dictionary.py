# Dictionary -> key(การเข้าถึงข้อมูล), value(ค่าของข้อมูล)
# การสร้าง dict
# my_dict = {key:value,key:value,key:value}
colors = {"red":"สีแดง","green":"สีเขียว","blue":"สีฟ้า"}
city = {1:"Bangkok",2:"Chaingmai"}
print(colors["red"]) #ระบุ key จะได้ value
print(city[1]) 
"""
drive = dict(file=1,internet=2,window="pc")
print(drive["window"])
print(colors.get("blue"))
colors.update({"yellow":"สีเหลือง"})
for item in colors:#จะได้ key
for item in colors.keys: #จะได้ key
for item in colors.values: #จะได้ value
for item in colors.items: #จะได้ key,value
for k,v in colors.items: #จะได้ key,value
"""
# change
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car.get("year"))

# add
car["color"] = "white"

# delete
## del colors = delete all

print(colors)
colors.pop("red") #specific
colors.popitem() #deleted lastest
print(colors)

## Dict of dict

shop = {
    "Starbuck":{
        "name" : "barista",
        "menu" : ["coffee","bread"],
        "zone" : "Supermarket"
    },
    "Mac":{
        "name" : "worker",
        "menu" : ["burger","soda"],
        "zone" : "Roadside"
    },
    "Coldstone":{
        "name" : "coldman",
        "menu" : ["Iceream","Softserve"],
        "zone" : "Market"
    },
}

print(shop)
print(shop["Coldstone"])
print(shop["Coldstone"]["menu"])
print("coffee" in shop["Starbuck"]["menu"])