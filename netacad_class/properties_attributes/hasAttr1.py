class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2



example_object = ExampleClass()
#hasattr() metoduyla bir class ya da object içinde istenilen değişkenin var olup olmadığını öğrenebiliriz.
print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))

