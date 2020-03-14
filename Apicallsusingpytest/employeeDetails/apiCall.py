import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = "{\"name\":\"sample test\",\"salary\":\"123\",\"age\":\"23\"}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))

