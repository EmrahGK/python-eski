print("""***********************************
. : Kullanıcı Girişi : .
***********************************
""")

sys_kullanıcı_adı = "EmrahGK"
sys_parola = "52345234A"

kullanıcı_adı = input("Kullanıcı adı: ")
parola = input("Parola: ")


if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("Parola Hatalı...")

elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print("Kullanıcı adı hatalı..")

elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("Kullanıcı adı ve Parola Hatalı..")

else:
    print("Sisteme giriş yaptınız. Ana sayfaya yönlendiriliyorsunuz..")