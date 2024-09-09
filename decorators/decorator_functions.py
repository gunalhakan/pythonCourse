# def sabah():
#     print("selam")
#     print("günaydın")
#     print("iyi günler")
# def aksam():
#     print("selam")
#     print("iyi akşamlar")
#     print("iyi günler")

# sabah()
# aksam()

# decorator functions fonksiyon öncesinde ve sonrasında 
# çalışacak standart işlemler için kolaylık sağlar

# Yukarıdaki yerine alt kısıım kullanılarak kod tekrarından kurtuluruz.

# selamlama içine fonksiyon parametre olarak gönderildi
# def selamlama(fn):
#     def wrapper():
#         print("selam")
#         fn()
#         print("iyi günler")
#     return wrapper

# def sabah():
#     print("günaydın")
# def aksam():
#     print("iyi akşamlar")

# # Fonksiyon içinde fonksiyon çağırıldı ve parametre olarak fonksiyon gönderildi
# s = selamlama(sabah)
# a = selamlama(aksam)

# s()
# a()


def selamlama(fn):
    def wrapper():
        print("selam")
        fn()
        print("iyi günler")
    return wrapper

# Decorator ile fonksiyon içindeki fonksiyonu çağırma işlemi kısaltılır.
@selamlama
def sabah():
    print("günaydın")
@selamlama
def aksam():
    print("iyi akşamlar" )

# Decorator kullanıldığı için selamlama üzerinden sabah fonksiyonu ile wrapper çalıştırılır.
sabah()
aksam()