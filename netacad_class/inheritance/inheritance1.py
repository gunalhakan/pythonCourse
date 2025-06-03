class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        # super() ile üst class ın init ine ulaşabiliyoruz.
        super().__init__(name)

    def ekle(self):
        return self.name + " ( * "
obj = Sub("Mahmut")

print(obj)

print(obj.ekle())
    