class Classy:
    pass

# class ismini döndürür
print(Classy.__name__)
obj = Classy()
# __name__ class ismini döndürür, object üzerinden döndürmek için type kullanılmak zorundadır
print(type(obj).__name__)
    
# Tüm modül isimleri __main__ dir. __main__ aslında çalışan dosyanın ismidir.
print(Classy.__module__)
obj = Classy()
print(obj.__module__)


class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne):
    pass
        
# __base__ hangi sınıftan türediğini gösterir. Eğer sadece object yazıyorsa bir sınıftan türememiştir.
print(Sub.__base__)
print(Sub.__base__.__name__)