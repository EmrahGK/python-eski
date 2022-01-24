#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam
# ne kadar ödemesini gerektiğini hesaplayın.


print("_ -  Yakıt maliyet Hesaplama Aracı - _ \n")

yakıt = float(input("Aracın Km'de kaç ₺ harcadığını girin: "))
yol = float(input("Aracın kaç km yol yaptığını girin: "))

print("Aracınız bu güzergahta toplam {}₺'lık yakıt harcamıştır.".format(yakıt * yol))
