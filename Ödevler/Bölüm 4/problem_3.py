print("""***************************************
      Harf Notu Hesaplama Aracı
***************************************
""")

vize1 = int(input("Vize 1: "))

vize2 = int(input("Vize 2: "))

final = int(input("Final: "))

genel_not = vize1 * 3/10 + vize2 * 3/10 + final * 4/10



print("\nPuanınız: ",genel_not)



if (genel_not >= 90):
    print("Harf Notunuz: AA")

elif (genel_not >= 85):
    print("Harf Notunuz: BA")

elif (genel_not >= 80):
    print("Harf Notunuz BB")

elif (genel_not >= 75):
    print("Harf Notunuz CB")

elif (genel_not >= 70):
    print("Harf Notunuz CC")

elif (genel_not >= 65):
    print("Harf Notunuz DC")

elif (genel_not >= 60):
    print("Harf Notunuz DD")

elif (genel_not >= 55):
    print("Harf Notunuz FD")

elif (genel_not < 55):
    print("Harf Notunuz FF")