# deserialize
# Ham bir datayı dictionary türüne çevirip kullanma işlemine deserialize işlemi denir.

import json

#json dosyasından veri almak için alttaki kod çalıştırılır
# with open("person.json") as file:
#     data = json.load(file)
with open("json/person.json") as file:
    #json dosyasından veri almak için json.load() metodu kullanılır.
    data = json.load(file)
# json-string

# data = """
#     {
#         "firstName": "Hakan",
#         "lastName": "Günal",
#         "hobbies": [
#         "spor",
#         "sinema"
#         ],
#         "age": 37,
#         "children": [
#             {
#             "firstName": "Nil",
#             "age": 9,
#             "hobbies":["müzik","spor","kitap"]
#             }
#         ]
#     }
#     """
# String halinde bir değişkenden almak için json.loads() metodu kullanılır.
# data = json.loads(data)

print(data)
print(type(data))
print(data["firstName"])
print(data["hobbies"])
print(data["hobbies"][0])