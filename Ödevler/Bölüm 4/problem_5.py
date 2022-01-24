"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak
istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan
bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan
bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs()
fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""
print("""*****************************
Geometrik Şekil Hesaplama Aracı
Lütfen Dörtgen veya Üçgen girin.
*****************************
""")

şekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz: ")

if (şekil == "Dörtgen" or şekil == "dörtgen"):
    print("\nLütfen kenarları sırayla girin: ")
    a = int(input("Birinci Kenar: "))
    b = int(input("İkinci Kenar: "))
    c = int(input("Üçüncü Kenar: "))
    d = int(input("Dördüncü Kenar: "))

    if (a == b and a == c and a == d):
        print("Girdiğiniz Şekil Karedir.")

    elif (a == c and b == d):
        print("Girdiğiniz Şekil Dikdörtgendir.")

    else:
        print("Kenarları sırayla ve doğru sgirdiğinizden emin olun..")

elif (şekil == "Üçgen" or şekil == "üçgen"):
    a = int(input("Birinci Kenar: "))
    b = int(input("İkinci Kenar: "))
    c = int(input("Üçüncü Kenar: "))

    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Girdiğiniz Şekil Eşkenar Üçgendir.")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("Girdiğiniz Şekil İkizkenar Üçgendir.")
        else:
            print("Girdiğiniz Şekil Çeşitkenar Üçgendir.")
    else:
        print("Bu Kenarlar Bir Üçgen belirtmiyor.")

else:
    print("\nŞekil İsmini Doğru Girdiğinizden Emin olun (Dörtgen ve Üçgen)")