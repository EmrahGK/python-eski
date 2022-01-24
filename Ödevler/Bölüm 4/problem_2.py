"""Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın."""


print("""*************************************
En büyük sayıyı hesaplama aracı.
*************************************
""")


sayi1 = int(input("Birinci sayı: "))

sayi2 = int(input("İkinci sayı: "))

sayi3 = int(input("Üçüncü sayı: "))


if (sayi1 >= sayi2 and sayi1 >= sayi3):
    print("En büyük sayı: ",sayi1)

elif (sayi2 >= sayi1 and sayi2 >= sayi3):
    print("En büyük sayı: ",sayi2)

elif (sayi3 >= sayi1 and sayi3 >= sayi2):
    print("En büyük sayı: ",sayi3)

else:
    print("Sayıları doğru girdiğinizden emin olun..")

