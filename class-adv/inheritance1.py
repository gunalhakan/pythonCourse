class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def intro(self):
        print("Kişi Bilgileri => ", self.name, self.surname, self.age)
# Person class ından student isminde yeni bir class oluşturuldu.
class Student(Person):
    pass
class Teacher(Person):
    pass
p1 = Person("Ali","Yılmaz",33)
s1 = Student("Esin","Güneş",12)
t1 = Teacher("Yavuz","Talın",29)
p1.intro()
# Student ve Teacher class ları türetildiği Person class ının tüm method ve 
# değişkenlerini(property) miras alır.
s1.intro()
t1.intro()



