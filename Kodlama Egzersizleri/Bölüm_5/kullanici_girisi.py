print("""
*******************************

Kullanıcı Girişi Programı

*******************************
""")


sys_kullanıcı_adı = "EmrahGK"

sys_şifre = "12345"

giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı adını girin: ")
    şifre = input("Şifreyi girin: ")


    if (sys_kullanıcı_adı != kullanıcı_adı and şifre == sys_şifre):
        print("Kullanıcı adını hatalı girdiniz. Lütfen tekrar deneyin")
        giriş_hakkı -=1

    elif (sys_kullanıcı_adı == kullanıcı_adı and şifre != sys_şifre):
        print("Parolayı hatalı girdiniz. Lütfen tekrar deneyin.")
        giriş_hakkı -= 1

    elif(sys_kullanıcı_adı != kullanıcı_adı and şifre != sys_şifre):
        print("Kullanıcı adı da şifre de hatalı. Tekrar deneyin")
        giriş_hakkı -= 1


    elif (giriş_hakkı == 0):
        print("Giriş hakkınız bitmiştir.")
        break

    else:
        print("Sisteme başarıyla giriş yaptınız.")
        break