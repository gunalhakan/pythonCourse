# serialize
# dictionary olan bir datayı string olan JSON ham veri türüne çevirme işlemine serialize denir.

import json

person = {
  "firstName": "Hakan",
  "lastName": "Günal",
  "hobbies": [
    "spor",
    "sinema"
  ],
  "age": 37,
  "children": [
    {
      "firstName": "Nil",
      "age": 9
    }
  ]
}

print(person)
print(person["firstName"])
print(type(person))
# karakter problemleri için ensure_ascii=False olmalıdır.
# sonuc = json.dumps(person, ensure_ascii=False,indent=2)

# print(sonuc)
# print(type(sonuc))

with open("json/person2.json","w") as file:
    json.dump(person,file, ensure_ascii=False,indent=2)