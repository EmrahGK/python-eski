a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b ** 2 - 4 * a * c

kok1 = (-b - delta ** 0.5 ) / (2 * a)
kok2 = (-b + delta ** 0.5 ) / (2 * a)

print("Birinci Kök: {}\nİkinci Kök: {}\n".format(kok1,kok2))