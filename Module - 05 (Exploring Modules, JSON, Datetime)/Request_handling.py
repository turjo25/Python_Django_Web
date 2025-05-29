#Request, Response cycle er 4 ta jinish handle krbo
#1.GET
#2.POST
#3.PUT/PATCH
#4.DELETE

import requests

#GET
response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.status_code)
# print(response.json())

#POST
data = {'userId': 1, 'id': 1, 'title':None}
response = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
# print(response.status_code)
# print(response.json())

#PUT
data = {'userId': 1, 'id': 1, 'title':'for testing PUT request'}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1",json=data)
# print(response.status_code)
# print(response.json())

#DELETE
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1",json=data)
print(response.status_code)
print(response.json())
