db = {
    "users": {
        "gunalhakan": {
            "firstName":"Hakan",
            "lastName":"Günal"
        },
        "akfomc": {
            "firstName":"Akif",
            "lastName":"Özmercan"
        }
    },
    "products": {
        "1": {
            "productName":"IPhone 13",
            "price":35000
        },
        "2": {
            "productName":"IPhone 14",
            "price":40000
        }
    }
}

import json

with open("json/db.json","w") as file:
    json.dump(db,file,ensure_ascii=False,indent=2)

with open("json/db.json") as file:
    db = json.load(file)

print(db["users"])
print(db["products"])

# print(db["users"]["gunalhakan"]["firstName"])
# print(db["products"]["1"]["productName"])
# print(db["products"]["1"]["price"])

db["products"].update({
    "3": {
            "productName":"IPhone 15",
            "price":45000
        }
})

db["users"].update({
    "gencNeslihan": {
            "firstName":"Neslihan",
            "lastName":"Genç"
        }
})

with open("json/db.json","w") as file:
    json.dump(db,file,ensure_ascii=False,indent=2)