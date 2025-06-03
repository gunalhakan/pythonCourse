class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2) #sınıfa varsayılan eleman atanabilir

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5
example_object_1.__first=999 # eski veri değiştirilmez aynı değişken ismiyle yeni veri eklenir.


print(example_object_1.__dict__) # __dict__ metoduyla {_sınıfismiDeğişkenismi:değer} şeklinde object bilgileri __(private) yazdırılır.
print(example_object_2.__dict__)
print(example_object_3.__dict__)
    