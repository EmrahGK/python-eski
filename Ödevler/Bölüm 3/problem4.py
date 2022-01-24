#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

ad = str(input("Lütfen adınızı girin: "))
soyad = str(input("Lütfen Soyadınızı girin: "))
no = str(input("Numaranızı yazınız. +90\t"))

print("Adınız {}, Numaranız da +90 {}. Doğru mu ?".format(ad +" "+ soyad,no))