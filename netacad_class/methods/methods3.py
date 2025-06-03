class Classy:
    # constructor __init__ metodudur. 
    # sadece object oluşturulurken bir kere çağırılır, class içinden bir daha çağırılamaz
    # __init__ değer döndürmez
    def __init__(self, value):
        self.var = value
        


obj_1 = Classy("object")

print(obj_1.var)
    