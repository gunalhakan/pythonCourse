class Classy:
    def visible(self):
        print("visible")
    # isminin başında __ olan metotlara class dışından erişim (kısmen) yoktur
    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()

