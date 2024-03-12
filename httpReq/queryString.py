import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos", params={
    "userId" : 1,
    "completed" : "true"
})
#print(response.text)
filterTodos = json.loads(response.text)

for todo in filterTodos :
    print(todo["title"]," - ",todo["completed"])

