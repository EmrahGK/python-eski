print("""
****************************************

Faktoriyel Hesaplama Aracı

(Çıkmak için Q'ya basın.)

****************************************""")



while True:
    sayi = input("Lütfen Faktoriyeli hesaplanacak sayıyı girin: ")

    if(sayi == "q"):
        print("Program Sonlanıyor...")

    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1):
            print("Faktoriyel",faktoriyel,"i'nin değeri: ",i5)
            faktoriyel *= i

        print("Faktoriyel Değeri: ",faktoriyel)
