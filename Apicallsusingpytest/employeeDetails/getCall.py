import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = "{\"name\":\"test\",\"salary\":\"123\",\"age\":\"23\"}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

