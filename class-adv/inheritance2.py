class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age)


# Student class ı Person fiyatından türetildi.
class Student(Person):
    pass
# Teacher class ı Person fiyatından türetildi.
class Teacher(Person):
    pass

p1 = Person("Ahmet","Turan",20)
p1.intro() # person

s1 = Student("Ali","Yılmaz",25)
# Student nesnesi Person dan türetildiği için Person içindeki metodlara ulaşabilir
s1.intro() # student

t1 = Teacher("Can","Yılmaz",25)
# Teacher nesnesi Person dan türetildiği için Person içindeki metodlara ulaşabilir
t1.intro() # teacher