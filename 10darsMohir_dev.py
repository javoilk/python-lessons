#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
    #if car.lower =='gm':
        #print(car.upper)
    #else:
        #print(car.lower)

#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
        #for car in cars:
            #if car != "GM":
                #print(car.title)
            #else:
                #print(car.upper)

#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
#login = input("Login kiriting! ")
#if login.lower == "admin":
    #print("Xush kelibsiz, Admin Foydalanuvchilar royxatini ko'rasizmi? ")
#else:
    #print(f"Xush kelibsiz, {login.title()}!")

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
print("Ikkita son kirting!")
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x == y:
    print("Sonlar teng ekan")
else:
    print("Sonlar teng emas ekan")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
son = float(input("Istalgan son kiriting: "))
if son <=0:
    print("Musbat son")
else:
    print("Manfiy son")

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
son = float(input("Son kiriting! "))
if son <=0:
    print(son **2)
else:
    print("Musbat son kiriting!")

