def ikiKez(fn):
    # iki fonksiyonda farklı sayıda parametre var, args ve kwargs bu yüzden kullanıldı
    def wrapper_iki(*args,**kwargs):
        fn(*args,**kwargs)
        fn(*args,**kwargs)
    return wrapper_iki

@ikiKez
def selam():
    print("Merhaba")
@ikiKez
# wrapper a içindeki fonksiyonda kullanılacak parametreler alttaki şekilde gönderildi
def selamIsim(isim):
    print("Merhaba",isim)

    
selam()
selamIsim("Mehmet")
