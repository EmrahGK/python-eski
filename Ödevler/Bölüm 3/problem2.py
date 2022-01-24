#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m) (kilo bölü boy karesi)

print(".: Boy Kitle Endeksi Hesaplama Aracı :.")
print("NOT: Boyunuzu girerken metre cinsinden girin. ör: 1.60.\n")

print("-------------------------------------------------------------------\n")

boy = float(input("Boyunuzu girin: "))
kilo = float(input("Kilonuzu girin: "))

index = ( kilo / (boy ** 2 ))

print("Vücut kitle endeksiniz: ",index)

print("\n\n18.5 ve altı Düşük Kilolu.")
print("18.5 - 24.9 Normal Kilolu.")
print("25-29.9 Fazla Kilolu.")
print("30-40 Obez.")
print("40+ Geçmiş olsun :).")