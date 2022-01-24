"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre
ekrana şu yazıları yazdırın.

Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

BKİ 18.5'un altındaysa -------> Zayıf

BKİ 18.5 ile 25 arasındaysa ------> Normal

BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

BKİ 30'un üstündeyse -------------> Obez """

print("""*********************************

Beden Kitle İndeksi Hesaplama Aracı

Lütfen Boyunuzu metre cinsinden girin.

*********************************

""")

boy = float(input("Boyunuzu girin: "))

kilo = int(input("Kilonuzu girin: "))

index = float(kilo / (boy ** 2))

print("Boyu {} ve Kilosu {} olan birinin BKİ'si: {}.".format(boy,kilo,index))


if (index >= 10 and index < 18.5 ):
    print("Beden Kitle İndeksinize göre Zayıfsınız.")

elif (index >= 18.5 and index < 25):
    print("Beden Kitle İndeksinize göre Normalsiniz.")

elif (index >=25 and index < 30):
    print("Beden Kitle İndeksinize Göre Fazla Kilolusunuz.")

elif (index >= 30):
    print("Beden Kitle İndeksinize Göre Obezsiniz.")

else:
    print("Boyunuzu doğru girdiğinizden emin olun. Ör: 1.90, 1.50 gibi.")


