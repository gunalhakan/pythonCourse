data = [
    {
        "userName": "gunalhakan",
        "firstName": "Hakan",
        "lastName": "Günal"
    },
     {
        "userName": "akfomc",
        "firstName": "Akif",
        "lastName": "Özmercan"
    }
]

import json

user = {
        "userName": "gencNeslihan",
        "firstName": "Neslihan",
        "lastName": "Genç"
}

with open("json/users-list.json") as file:
    users = json.load(file)

for user in users:
    if user["userName"] == "gunal_hakan":
        user["userName"] = "gunalhakan"

users.remove(users[0])

# users.append(user)


with open("json/users-list.json","w") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)