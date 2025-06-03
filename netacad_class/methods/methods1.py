class Classy:
    # Class içindeki her metodun ilk parametresi self olmak zorunda
    varia = 2
    #self parametresi class ve instance değişkenlere erişmek için kullanılabilir.
    def method(self):
        # print(varia) self olmadan kullanıldığı için bu kod hata verir
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()

