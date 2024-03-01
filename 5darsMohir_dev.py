#Quyidagi o'zgaruvchilarni yarating: 
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
print(kocha + ' ' + "ko'chasi,", mahalla + ' ' + "mahallasi,", tuman + ' ' + "tumani,",viloyat + ' ' + "viloyati,")
#Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha = input("Kochangiz nomi? ")
mahalla = input("Mahalla nomi? ")
tuman = input("Tuman nomi? ")
viloyat = input("Viloyat nomi? ")
print(kocha + ' ' + "ko'chasi,\n", mahalla + ' ' + "mahallasi,\n",tuman + ' ' + "tumani,\n", viloyat + ' ' + "viloyati\n")
#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print(kocha + ' ' + "ko'chasi,\n", mahalla + ' ' + "mahallasi,\n",tuman + ' ' + "tumani,\n", viloyat + ' ' + "viloyati\n")
#Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
kocha="Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
yangi_manzil = (f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani,{viloyat} viloyati,")
print(yangi_manzil)
#manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
kocha= "Bog'bon"
print(kocha.upper())
ism = "javohir ilkhomjonov"
print(ism.title())
ism_ = "javohir ilkhomjonov"
print(ism_.capitalize())
kocha= "Bog'bon"
print(kocha.lower())

