import requests

def test_post_data():
 url="http://dummy.restapiexample.com/api/v1/employees"
 payload = "{\"employee_name\": \"kokila\", \"employee_salary\": \"20000\", \"employee_age\": \"22\"}"
 headers = {
  "Content-Type": "application/json"
 }
 response = requests.request("POST", url, headers=headers, data=payload)
 print(response.text)
 print(response.status_code)