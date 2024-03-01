#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.\

#son = input("Juft son kiriting: ")
#if son%2:
    #print("Bu son juft emas!")
#else:
    #print("Raxmat")



#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

#yosh = int(input("Yoshingizni kiriting: "))
#if yosh<=4 or yosh>=60:
    #print("Bepul")
#elif yosh<=18:
    #print("10000 so'm") 
#elif yosh>18:
    #print("20000 so'm")

#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
    
son_x = float(input("Birinchi sonni kiriting: "))
son_y = float(input("Ikkinchi sonni kiriting: "))
if son_x == son_y:
   print("{son_x}={son_y}")
elif son_x > son_y:
   print("{son_x}>{son_y}")
else:
   print("{son_x}<{son_y}")


#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar = ["anor","bexi","olma","banan","uzum","gosht","kolbasa","qaymoq","non","saryog'"]
yangi_savat = []
for n in range(5):
   yangi_savat.append(input(f"Savat {+1}-mahsulotni qoshing"))
for mahsulot in mahsulotlar:
   print(f"Dokonimizda {mahsulot} bor")
else:
   print(f"Dokonimizda {mahsulot} yoq")



#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
   
foydalanuvchilar = ['anvar','kamol','javo','joxa','xoji']
login = input("Yangi login tanlang: ")
if  login not in foydalanuvchilar:
    print("Xush kelibsiz {login}")
else:
   print("login band yangi login tanlang")

#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 

son = int(input("Istalgan butun son kiriting: "))
for n in range(2,11):
   if not son%2:
      print(f"{son} soni {n} qoldiqsiz bo'linadi")
   