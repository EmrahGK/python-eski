print("""
*****************************

ATM MAKİNESİ

İşlemler:

1. Bakiye sorgulama

2. Para Yatırma

3. Para Çekme

(Programdan çıkmak için Q'ya basın)

*****************************""")

bakiye = 1000

while True:
    işlem = input("\nİşlemi seçiniz: ")

    if( işlem == "q" or "Q"):
        print("Görüşürüz..")
        break

    elif(işlem == "1"):
        print("\nBakiyeniz: {}₺'dir".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("\nLütfen yatırılacak m  iktarı girin: "))

        bakiye += miktar

        print("\nBakiyeniz artık {}₺'dir.".format(bakiye))

    elif(işlem == "3"):
        miktar = int(input("\nLütfen çekilecek miktarı girin: "))

        if(bakiye - miktar < 0):
            print("\nParayı çekemezsiniz, lütfen bakiyenizden fazla para çekme talebi oluşturmayın.")
            continue

        bakiye -= miktar

        print("\nBakiyeniz artık {}₺'dir..".format(bakiye))

    else:
        print("\n\nLütfen geçerli bir işlem giriniz...\n")
