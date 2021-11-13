print ("Program Mencari Bilangan Terbesar Dari 3 Bilangan")

a = int(input("Masukan Bilangan Pertama: "))
b = int(input("Masukan Bilangan Kedua: "))
c = int(input ("Masukan Bilangan Ketiga: "))

if a > b > c :
    print("Bilangan pertama Adalah Terbesar = %s" % a)
elif b > c :
    print("Bilangan Kedua Adalah Bilangan Terbesar = %s" % b)
else :
    print("Bilangan ketiga Adalah Bilangan Terbesar = %s" % c)

