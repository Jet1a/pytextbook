
#String Deep

name = "OpzTV" #index ตัวแรก เริ่มที่ => 0

# ช่องว่างในข้อความก็นับเป็น index

print (name[0:3]) #[เริ่ม:ก่อนถึงตัวจบ]
# จะได้ Op ถ้า จบที่ 4 จะได้ Opz

name = "OpzTV : 10" 
print(name[-2]) # จะนับจากหลัง จะได้ 1
print(name[-2:]) # จะนับต่อ จะได้ 10

name = " OpzTV"
print(len(name)) #นับ Index
name=name.strip() # Strip ลบช่องว่าง
print(len(name))

name = "OpzTV"
print(name.upper()) #ตัวพิมพ์ใหญ่
print(name.lower()) #ตัวพิมพ์เล็ก
print(name.capitalize()) #ตัวพิมพ์ใหญ่ตัวแรกสุดเท่านั้น

name = "OpzTV"
print(name.replace("Opz","Breakgate")) #แทนที่ [old,new,count] count หากมีซ้ำหลากอันแล้วอยากแทนแค่บางลำดับ
name = "OpzTV 3 3 3"
print(name.replace("3","5",2))

name = "OpzTV"
i = "TV" in name #เช็ค " " ในตัวแปรมั้ย จะได้ => true false
i = "TV" not in name
print(i)

fname = "Krit"
sname = "Banki"
age = "20"
fullname = fname + sname + age #ต่อstring
print(fullname,"\t789") #\t == tab

fname = "Krit"
sname = "Banki"
age = "20"
inc = 13659.455423
txt = "First name : {0}\tLast name : {1}\tage : {2} \tIncome :{3:.3f}" #เลขตามลำดับ
print(txt.format(fname,sname,age,inc)) #การใช้ format {}

name = "Mr.Chicken"
if name.startswith("Mr"): #check started word
    print("Male")
elif name.endswith("ed"): #check ended word
    print("Past")
else :
    print("Undefined")