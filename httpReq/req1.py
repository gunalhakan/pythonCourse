import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code)
#print(response.headers)
print(response.encoding)
#print(response.headers["Content-Type"])
print(response.url)
#print(response.text)
users = json.loads(response.text)
#print(users)
print(users[0]["name"])
for user in users:
    print(user["name"])

