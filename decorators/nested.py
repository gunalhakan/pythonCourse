
# encapsulation 
# dıştaki işlemler, çağırılmadığı sürece içteki fonksiyon ile karışmaz
# karmaşık işlemlerde ayırt etme ve scope ları ayarlamak için kullanılabilir.
# inner a dışardan ulaşılamaz, sadece outer ın içinden ulaşılabilir

# def outer(num1):
#     print("outer")
    
#     def inner(num1):
#         print("inner")
#         return num1 + 1
#     num2 = inner(num1)
#     print(num1,num2)
# outer(4)
    

# faktoriyel işlemi
# encapsulation ile veri kontrolü ve hesaplama birbirinden ayrıldı

def factorial(num):
    # Faktoriyel işlemi için doğru veri kontrolü dış fonksiyonda yapıldı
    if not isinstance(num,int):
        raise TypeError("sayı integer türünden olmalı")
    if not num >= 0:
        raise ValueError("sayı 0 dan büyük olmalı") 
    # inner bu kısımda kendi içinde çalışarak dıştaki fonksiyonla karışmaz
    # faktoriyelin hesaplaması içte yapıldı
    def inner_factorial(num):
        if num <= 1:
            return 1
        return inner_factorial(num -1 ) * num
    # outer dan dışarı döndür
    return inner_factorial(num)
try :
    print(factorial("-5"))
except Exception as e:
    print(e)