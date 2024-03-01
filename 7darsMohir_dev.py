#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ["Xoji","Jonibek","Ali"]
print("Salom",ismlar[0],"bugun choyxona bormi? ")
print(ismlar[1],"choyxonaga boramizmi? ")

#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).

sonlar = [2,-2,5.0,5000]
print(sonlar)

#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 

print(sonlar[0] * sonlar[2])
print(sonlar[2] / sonlar[3])
print(sonlar[3] + sonlar[1])
print(sonlar[0] - sonlar[1])

#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 

t_shaxslar = [
    "Imom Buxoriy",
    "Mirzo Ulug'bek",
    "Amir Temur"
]

z_shaxslar = [
    "Bill Gates",
    "Steve Jobs",
    "Elon Musk"
]

#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:


print("Men tarixiy shaxslardan",t_shaxslar.pop(0), "bilan\n""zamonviy shaxslardan esa",z_shaxslar.pop(2),"bilan suxbat qilishni istar edim")


#friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 

friends = []
friends.append("Xoji")
friends.append("Maxmit")
friends.append("Mirzo")
friends.append("Murod")
friends.append("Paxlavon")
print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlanng
friends.remove("Xoji")
friends.remove("Maxmit")
print(friends)
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0,"Shox")

#Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

mehmonlar =[]
mehmonlar.append(friends.pop(0))
print("Kelgan mexmonlar:" , mehmonlar)