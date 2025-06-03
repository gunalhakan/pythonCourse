class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        # self class içindeki diğer metodları çağırmak için kullanılır.
        
        self.other()
    

obj = Classy()
obj.method()

