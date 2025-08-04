import json
import math
Filename = "bank.json"
def royxat():
    with open(Filename, "r") as file:
        return json.load(file)
# Bu balans qismi
def balans(username):
    miqdor = int(input("Qancha pul qo‘shmoqchisiz? "))

    foydalanuvchilar = royxat()

    for i in foydalanuvchilar:
        if i["username"] == username:
            if "balance" not in i:
                i["balance"] = 0
            i["balance"] += miqdor
            print(f"Yangi balans: {i['balance']} so‘m")
            break

    with open(Filename, "w") as file:
        json.dump(foydalanuvchilar, file)

def user_ozgar(old_username):
    yangi_username = input("Yangi usernameni kiriting: ")

    foydalanuvchilar = royxat()

    for i in foydalanuvchilar:
        if i["username"] == yangi_username:
            print("Bu username allaqachon mavjud, boshqasini tanlang.")
            return old_username

    for i in foydalanuvchilar:
        if i["username"] == old_username:
            i["username"] = yangi_username
            print(f"Username muvaffaqiyatli o‘zgartirildi: {yangi_username}")
            break

    with open(Filename, "w") as file:
        json.dump(foydalanuvchilar, file)

    return yangi_username


def xizmatlar(username):
    while True:
        print("1. balansni o`zgartirish")
        print("2. usernameni ozgartish")
        print("2. parolni ozgartirish")
        print("0. To‘xtatish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            balans(username)
        elif tanlov == "2":
            username=user_ozgar(username)
        elif tanlov == "3":
           if royhatdan_otish():
               print("royxatdan otish boshlandi")
        elif tanlov == "0":
            print(" Dastur to‘xtatildi.")
            break
        else:
            print("Noto‘g‘ri tanlov.")

def kirish():
    username = input("usernameni kiriting: ")
    password = input("passwordni kiriting: ")
    foydalanuvchilar = royxat()

    for i in foydalanuvchilar:
        if i['username'] == username and i['password'] == password:
            print("Muvaffaqiyatli kirdingiz.")
            return username

    print("User yoki parol xato.")
    return None
def royhatdan_otish():
    username = input("usernameni kiriting: ")
    password = input("passwordni kiriting: ")
    balanse = input("balansingizni kiriting")

    foydalanuvchilar = royxat()

    for i in foydalanuvchilar:
        if i["username"] == username:
            print("Bu username mavjud, iltimos boshqasini kiriting.")
            return


    yangi_foydalanuvchi = {
        "username": username,
        "password": password,
        "balanse": balanse
    }

    foydalanuvchilar.append(yangi_foydalanuvchi)


    with open(Filename, "w") as file:
        json.dump(foydalanuvchilar, file)

    print("Ro‘yxatdan o‘tish muvaffaqiyatli yakunlandi!")



def boshlash():
    while True:
        print("\n Bankimizga xush kelibsiz!")
        print("1. Kirish")
        print("2. Ro‘yxatdan o‘tish")
        print("0. To‘xtatish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            username = kirish()
            if username:
                xizmatlar(username)

        elif tanlov == "2":
           royhatdan_otish()

        elif tanlov == "0":
            print(" Dastur to‘xtatildi.")
            break
        else:
            print("Noto‘g‘ri tanlov.")
boshlash()







