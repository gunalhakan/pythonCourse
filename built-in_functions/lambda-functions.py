# def multiply_2(a):
#     return a * 2
# sonuc = multiply_2(5)
# print(sonuc)

multiply = lambda b : b * 3
sonuc = multiply(10)
print(sonuc)

toplam = lambda a,b,c : a+b+c
sonuc2 = toplam(15,20,25)
print(sonuc2)

tersCevir = lambda kelime : kelime[::-1]
sonuc3 = tersCevir("ABCDEF")
print(sonuc3)

def myFunc(n):
    print()
    return lambda x : x * n

multi2 = myFunc(2) # myFunct fonksiyonuna giden değer yani n değeri
sonuc4 = multi2(10) # lambda ya giden değer yani x değeri 

print(sonuc4)