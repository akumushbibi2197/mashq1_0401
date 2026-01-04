#1-misol
import random
import string

uzunlik = int(input("Parol uzunligini kiriting: "))

belgilar = string.ascii_letters + string.digits + string.punctuation
parol = ""

for i in range(uzunlik):
    parol += random.choice(belgilar)

print("Yaratilgan parol:", parol)

#2-misol
import random

loto = random.sample(range(1, 51), 6)
print("Loto raqamlari:", loto)

#3-misol
from collections import Counter

fayl_nomi = input("Fayl nomini kiriting (masalan: matn.txt): ")

with open(fayl_nomi, "r", encoding="utf-8") as f:
    matn = f.read().lower()

sozlar = matn.split()
hisob = Counter(sozlar)

print("Eng ko‘p ishlatilgan 5 ta so‘z:")
for soz, soni in hisob.most_common(5):
    print(soz, "-", soni)

#4-misol
sonlar = input("Sonlarni bo‘sh joy bilan kiriting: ")
royxat = list(map(int, sonlar.split()))

natija = list(set(royxat))
print("Dublikatsiz ro‘yxat:", natija)

#5-misol
birlik = ["nol", "bir", "ikki", "uch", "to‘rt", "besh", "olti", "yetti", "sakkiz", "to‘qqiz"]
onlik = ["", "o‘n", "yigirma", "o‘ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to‘qson"]

son = int(input("0 dan 999 gacha son kiriting: "))

if son < 10:
    print(birlik[son])
elif son < 100:
    print(onlik[son // 10], birlik[son % 10])
else:
    yuz = son // 100
    qoldiq = son % 100
    if qoldiq == 0:
        print(birlik[yuz], "yuz")
    else:
        print(birlik[yuz], "yuz", onlik[qoldiq // 10], birlik[qoldiq % 10])
