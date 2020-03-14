import requests

url = "https://jsonplaceholder.typicode.com/posts/1"


headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers)

print(response.text.encode('utf8'))

