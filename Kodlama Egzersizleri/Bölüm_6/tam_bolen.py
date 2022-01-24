print("""
(Çıkmak için q'ye basın.)
""")

def tambölenleribulma(sayı):
    tam_bolenler = []
    sayınınfazlası = sayı + 1

    for i in range(1,sayınınfazlası):

        if( sayı % i == 0):
            tam_bolenler.append(i)

    return tam_bolenler

while True:
    sayı = input("\nLütfen bir sayı giriniz: ")

    if( sayı == "q"):
        print("Program sonlanıyor..")
        break
    else:
        sayı = int(sayı)
        print("Girdiğiniz sayının tam bölenleri: ",tambölenleribulma(sayı))



