data = {
    "gunalhakan": {
        "firstName":"Hakan",
        "lastName":"Günal"
    },
    "akfomc": {
        "firstName":"Akif",
        "lastName":"Özmercan"
    }
}

import json

with open("json/users-dictionary.json","w") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

with open("json/users-dictionary.json") as file:
    users = json.load(file)

print(users["gunalhakan"])
print(users["akfomc"])

users.update({
    "gencNeslihan": 
        {
            "firstName": "Neslihan",
            "lastName": "Genç",
            "age":30
        }
})

users.pop("gunalhakan")

with open("json/users-dictionary.json","w") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)