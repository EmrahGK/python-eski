print("""***********************************
Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi

2. Çıkarma işlemi

3. Çarpma İşlemi

4. Bölme İşlemi

***********************************
""")

a = int(input("Birinci sayı: "))

b = int(input("İkinci sayı: "))

işlem = input("İşlemi girin: ")

if işlem == "1":
    print("{} ile {} sayılarının toplamı: {}.".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} sayılarının farkı: {}.".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {} sayılarının çarpımı: {}.".format(a,b,a*b))
elif işlem == "4":
    print("{} ile {} sayılarının bölümü: {}.".format(a,b,a/b))

else:
    print("\nLütfen Geçerli bir işlem girin..")