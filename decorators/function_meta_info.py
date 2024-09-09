
def log_data(fn):
    def wrapper(*args,**kwargs):
        print(f"Çağırdığınız fonksiyon ismi: {fn.__name__}")
        print(f"Çağırdığınız fonksiyon açıklaması {fn.__doc__}")
        # fonksiyondan return ile gelen sonucu yazdırmak için alttaki return kullanılmalıdır.
        return fn(*args,**kwargs)
    return wrapper

@log_data
def add(s1,s2):
    """Gelen sayıları toplar"""
    return s2 + s1

print(add(10,20))