import requests

response = requests.post("https://jsonplaceholder.typicode.com/posts", data = { 

    "title": "test tilte",
    "body": "test body",
    "userId" : 1
    }
)
print(response)
print(response.text)
print(response.json())
print(response.headers)
