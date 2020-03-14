import requests

def test_delete_employees_check_status_code_equals_406():
 url = "http://dummy.restapiexample.com/api/v1/employees"

 response = requests.delete(url)

 print(response.status_code)

 assert response.status_code == 406


