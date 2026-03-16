from utils.son_tekshir import musbatmi
from utils.juft_toq import juftmi
from utils.hisoblash import hisobla
from utils.orta_qiymat import orta
from utils.eng_katta import top
from utils.matn_uzunlik import uzunlik
from utils.teskari_matn import teskari
from utils.parol_tekshir import kuchlimi
from utils.musbat_sonlar import filtr


while True:
    print("\n--- MENU ---")
    print("1 — son musbat yoki manfiyligini tekshirish")
    print("2 — juft yoki toq sonni aniqlash")
    print("3 — ikki son ustida amal bajarish")
    print("4 — sonlar ro‘yxatining o‘rtacha qiymatini topish")
    print("5 — ro‘yxatdan eng katta sonni topish")
    print("6 — matn uzunligini aniqlash")
    print("7 — matnni teskari qilish")
    print("8 — parol kuchliligini tekshirish")
    print("9 — musbat sonlarni ajratib olish")
    print("0 — dasturdan chiqish")

    tanlov = input("Tanlovni kiriting: ")

    if tanlov == "1":
        son = float(input("Son kiriting: "))
        print(musbatmi(son))

    elif tanlov == "2":
        son = int(input("Son kiriting: "))
        print(juftmi(son))

    elif tanlov == "3":
        a = float(input("1-son: "))
        b = float(input("2-son: "))
        amal = input("Amal (+, -, *, /): ")
        print(hisobla(a, b, amal))

    elif tanlov == "4":
        sonlar = list(map(float, input("Sonlarni probel bilan kiriting: ").split()))
        print(orta(sonlar))

    elif tanlov == "5":
        sonlar = list(map(float, input("Sonlarni probel bilan kiriting: ").split()))
        print(top(sonlar))

    elif tanlov == "6":
        matn = input("Matn kiriting: ")
        print(uzunlik(matn))
    elif tanlov == "7":
        matn = input("Matn kiriting: ")
        print(teskari(matn))

    elif tanlov == "8":
        parol = input("Parol kiriting: ")
        print(kuchlimi(parol))

    elif tanlov == "9":
        sonlar = list(map(float, input("Sonlarni probel bilan kiriting: ").split()))
        print(filtr(sonlar))

    elif tanlov == "0":
        print("Dastur tugadi.")
        break

    else:
        print("Noto‘g‘ri tanlov! Qaytadan urinib ko‘ring.")
