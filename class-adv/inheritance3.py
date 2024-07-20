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
    def __init__(self, name, surname, age,number):
        # Person nesnesindeki init i çağır, tüm elemanları yeniden yazma
        # Person.__init__(self, name, surname, age)

        # Person yerine super metodu kullanılabilir, 
        # super metoduyla self i de kullanmayı da kaldırabiliriz
        super().__init__(name, surname, age)
        self.number = number
        print("Student nesnesi türetildi")
    # parent sınıfındaki aynı isimle üretilen metod, parent metodunu bastırır
    def intro(self):
        print(self.name, self.surname, self.age, self.number)
    def study(self):
        print(f"{self.number} numaralı öğrenci {self.age} yaşındadır.")
# Teacher class ı Person fiyatından türetildi.
class Teacher(Person):
    def __init__(self, name, surname, age,branch):
        super().__init__(name, surname, age)
        self.branch = branch
        print("Teacher nesnesi türetildi")

    def teach(self):
        print(f"{self.name} isimli öğretmen {self.branch} dersine giriyor")

p1 = Person("Ahmet","Turan",20)
p1.intro() # person

s1 = Student("Ali","Yılmaz",15,"243")
s1.study() # student

t1 = Teacher("Can","Yılmaz",25,"coğrafya")
t1.teach() #teacher