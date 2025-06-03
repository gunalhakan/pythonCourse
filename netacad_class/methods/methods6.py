class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

# python da bir nesnenin değeleri runtime içinde öğrenilir ve değiştirilebilir.
# aşağıda bir nesneye ait başharfi i ile başlayan değişkenler tespit edilip, 
# türü int olanlara bir eklenir.

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
    