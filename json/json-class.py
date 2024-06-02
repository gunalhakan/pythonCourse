class Product:
    def __init__(self,name,price,id):
        self.name = name
        self.price = price
        self.id = id

p1 = Product("Macbook M1 Air 13",35000,"p1")
p2 = Product("Macbook M2 Pro 13",46000,"p2")

# class tan türetilen bir object i dictionary e çevirmek için __dict__ kullanılır.

# products = [p1.__dict__,p2.__dict__]
products = {p1.id : p1.__dict__,p2.id : p2.__dict__}

import json

with open("json/products.json","w") as file:
    json.dump(products,file,ensure_ascii=False,indent=2)

with open("json/products.json") as file:
    data = json.load(file)

# urunler = []
# print(data)
# print(data["p1"]["name"])

urunler = {}

for key,value in data.items():
    
    urunler.update({
        key : {
            "name" : data[key]["name"],
            "value" : data[key]["price"]
        }
    })
    
print(urunler)

    