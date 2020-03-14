import requests

url = " https://jsonplaceholder.typicode.com/posts/1"

payload = "{\"name\":\"test1\",\"salary\":\"123\",\"age\":\"23\"}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text.encode('utf8'))