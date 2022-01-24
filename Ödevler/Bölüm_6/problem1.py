"""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel
olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel
bir sayıdır (1 + 2 + 3 = 6).
"""

def bölenler(sayı):
    tam_bolenler = []
    sayınınfazlası = sayı + 1

    for i in range(1, sayınınfazlası):

        if (sayı % i == 0):
            tam_bolenler.append(i)

    return tam_bolenler


while True:
    sayı = int(input("Lütfen bir sayı girin: "))


    print("\nGirdiğiniz sayının bölenleri: ",bölenler(sayı))


