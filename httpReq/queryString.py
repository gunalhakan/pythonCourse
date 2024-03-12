import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos", params={
    "userId" : 1,
    "completed" : "true"
})

print(response.text)
