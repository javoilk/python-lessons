#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ["Xoji","Paxlavon","Mexmet","Mirzo","Bexruz"]
for ism in ismlar:
    print("Salom",ism)

#Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
    print(f"kod{len(ismlar)},marta takrorlandi")

#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(10,100))
for son in sonlar:
    print(son**2)

#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
sevimli_kinolar = []
print("5 ta eng sevimli kinoyingizni kiriting? ")
for n in range(5):
    sevimli_kinolar.append(input(f"{n+1} Kino: "))
    print(sevimli_kinolar)

#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

s_odamlar = input("Bugun necha kishi bilan suhbat qildingiz? ")
suhbatlashgan_odamlar = []
for n in range(s_odamlar):
    suhbatlashgan_odamlar.append(input(f"{s_odamlar+1}-suhbat qilgan odamingiz kim edi? "))
    print(suhbatlashgan_odamlar)