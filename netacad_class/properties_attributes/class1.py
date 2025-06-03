class ExampleClass:
    counter = 0 # class property
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

# Her nesne tarafından ulaşılabilir değişkenlerdir. Nesne oluşturulmadan önce varlardır.
#class properties ler __dict_ ile görüntülenmezler, dışardan ulaşılabilir. 
# Ayrıca dışardan atama yapıldığında object için farklı değer alır.
# Örnek : eexample_object_1.counter= 999 
# Dışardan atama yapılmadığında her nesne için aynı değeri alır.

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)


print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)